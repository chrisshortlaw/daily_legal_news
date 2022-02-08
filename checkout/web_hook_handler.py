import json
from time import sleep
from typing import Dict

from django.http import HttpResponse
from django.core.mail import send_mail

from django.contrib.auth.models import User, Group

from user_profiles.models import Profile
from subscriptions.models import Subscription, SubscriptionProduct


class StripeWebHookHandler:
    '''
    Handles Stripe webhooks
    '''

    def __init__(self, request):
        self.request = request

    def handle_webhook(self, event):

        return HttpResponse(
                            content=f'handle_webhook: Webhook Received: {event["type"]}',
                            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''
        Handle the payment.intent webhook from stripe
        '''
        intent = event['data']['object']
        pay_id = intent.id
        # save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details

        user_exists = False
        attempt = 1
        # Checks 5 times if Order is in system
        while attempt <= 5:
            try:
                order = User.objects.get(
                        full_name__iexact=billing_details.name,
                        email__iexact=billing_details.email,
                        )
                user_exists = True
                break
            except User.DoesNotExist:
                attempt += 1
                sleep(1)
        if user_exists:
            return HttpResponse(
                    content=f'Webhook received: { event["type"] } | SUCCESS: Verified user in database',
                    status=200
                    )
        else:
            return HttpResponse(
                                content=f'Webhook received: {event["type"]}',
                                status=500
                                )

    def handle_payment_intent_failed(self, event):
        '''
        Handle the payment_intent.payment_failed webhook
        '''
        return HttpResponse(
                content=f'Payment Failed: Webhook Received: {event["type"]}',
                status=200
                )

    def handle_checkout_session_completed(self, event):
        '''
        Handles the Checkout_session webhook
        Locates user and adds them to the subscribers group
        '''

        checkout_session = event['data']['object']

        subscribed_user = process_user_profile(checkout_session)

        product = SubscriptionProduct.objects.get(id=checkout_session['metadata']['product_id'])

        if subscribed_user:
            add_user_to_subscriber_group(subscribed_user)
            new_sub = Subscription.objects.create(user=subscribed_user.user,
                                                  sub_product=product,
                                                  sub_id=checkout_session['subscription'],
                                                  subscription_status='active',
                                                  )
            new_sub.save()
            return HttpResponse(
                                content=f'Profile located. Webhook received: { event["type"] }',
                                status=200
                                )
        else:
            return HttpResponse(
                                content=f'{checkout_session["customer_name"]}User Profile could not be located',
                                status=500)

    def handle_cancel_subscription(self, event):

        subscription_session = event['data']["object"]

        cancelled_sub = Subscription.objects.get(sub_id=subscription_session["id"])

        subscriber_profile = Profile.objects.get(user = cancelled_sub.user)

        if subscriber_profile:
            remove_user_from_subscriber_group(subscriber_profile)
            cancelled_sub.status = 'cancelled'
            cancelled_sub.save()
            return HttpResponse(
                                content=f'Profile located. Subscription Cancelled: { event["type"] }',
                                status=200
                                )
        else:
            return HttpResponse(
                    content=f'{subscription_session["customer"]}: User Profile could not be located',
                                status=500)


def process_user_profile(stripe_session):
    '''
    Takes a stripe_session object, extracts relevant data
    Uses data to retrieve user_profile from db
    Returns user_profile
    '''
    stripe_objects = ['checkout.session', 'invoice', 'intent',
                      'plan', 'subscription', 'payment_intent']
    lookup_dict = {}

    if stripe_session.get('object') not in stripe_objects:
        # Check returned json (converted to dict) for value of 'object'
        if not isinstance(stripe_session, Dict):
            raise TypeError(f'Expected: Stripe object or Dict. Received: {stripe_session}')
        else:
            print('Stripe_session returned dictionary')
            if not set(stripe_objects).isdisjoint(stripe_session.keys()):
                if stripe_session.get('customer'):
                    lookup_dict['customer_id'] = stripe_session.get('customer')
                if stripe_session.get('subscription'):
                    lookup_dict['sub_id'] = stripe_session.get('subscription')
                if stripe_session.get('customer_email'):
                    lookup_dict['stripe_email'] = stripe_session.get('customer_email')
    else:
        if stripe_session.get('customer'):
            lookup_dict['customer_id'] = stripe_session.get('customer')
        if stripe_session.get('subscription'):
            lookup_dict['sub_id'] = stripe_session.get('subscription')
        if stripe_session.get('customer_email'):
            lookup_dict['stripe_email'] = stripe_session.get('customer_email')

    sub_user_profile = None

    user_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            if lookup_dict.get('stripe_email') is not None:
                sub_user = User.objects.get(email=lookup_dict.get('stripe_email'))
                sub_user_profile = Profile.objects.get(user=sub_user)
            user_exists = True
            break
        except Profile.DoesNotExist:
            attempt += 1
            sleep(1)
    if user_exists:
        return sub_user_profile
    else:
        return None


def add_user_to_subscriber_group(subscribing_user_profile):
    '''
    Takes a user_profile, retrieves user(one-to-one relationship),
    Retrieves subscriber group from db and adds user to that subscriber group

    '''
    if isinstance(subscribing_user_profile, User):
        subscriber = subscribing_user_profile
    elif isinstance(subscribing_user_profile, Profile):
        subscriber = subscribing_user_profile.user
    else:
        raise TypeError(f'{ subscribing_user_profile } must be of type User or Profile. Is of type {type(subscriber)}')

    SubscriberGroup = Group.objects.get(name='Subscriber')
    if subscriber in SubscriberGroup.user_set.all():
        return subscriber
    else:
        SubscriberGroup.user_set.add(subscriber)
        print(f'Successfully Added {subscriber} to Subscriber Group')
        return subscriber


def remove_user_from_subscriber_group(subscribing_user_profile):
    if isinstance(subscribing_user_profile, User):
        subscriber = subscribing_user_profile
    elif isinstance(subscribing_user_profile, Profile):
        subscriber = subscribing_user_profile.user
    else:
        raise TypeError(f'{ subscribing_user_profile } must be of type User or Profile. Is of type {type(subscriber)}')

    SubscriberGroup = Group.objects.get(name='Subscriber')
    SubscriberGroup.user_set.remove(subscriber)
    SubscriberGroup.save()
    subscriber.save()
    print(f'Successfully Removed {subscriber} to Subscriber Group')
    return subscriber.groups.all()


def update_subscription_from_webhook(webhook_user, event_dict):
    if isinstance(event_dict, Dict):
        event = event_dict['data']['object']
        if isinstance(webhook_user, User):
            if event.get('subscription'):
                sub = Subscription.objects.get(sub_id=event.get('subscription'))
            else:
                sub = Subscription.objects.get(user=webhook_user)
            if event.get('current_period_end'):
                sub.next_payment_date(event['current_period_end'])
            if event.get('subscription'):
                sub.sub_id = event['subscription']
            if event.get('current_period_start'):
                sub.last_payment_date(event['current_period_start'])
            if event.get('billing_cycle_anchor'):
                sub.payment_start_date(event['billing_cycle_anchor'])
            if event.get('status'):
                sub.subscription_status = event['status']
                sub.save()
        return webhook_user
    else:
        raise TypeError(f'{ event_dict } should be a dictionary type')
