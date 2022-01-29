import json
from time import sleep
from typing import Dict

from django.http import HttpResponse

from django.contrib.auth.models import User, Group

from user_profiles.models import Profile


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
        intent = event.data.object
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

        checkout_session = event.data.object

        subscribed_user, confirmation = process_user_profile(checkout_session)

        if confirmation:
            add_user_to_subscriber_group(subscribed_user)
            return HttpResponse(
                                content=f'Profile located. Webhook received: { event["type"] }',
                                status=200
                                )
        else:
            return HttpResponse(
                                content=f'{checkout_session.customer_name}User Profile could not be located',
                                status=500)

    def handle_invoice_updated(self, event):

        invoice_update_session = event.data.object

        subscriber_profile, found_profile = process_user_profile(invoice_update_session)

        if found_profile:
            subscriber_profile.next_payment_date(invoice_update_session.period_end)
            subscriber_profile.last_payment_date(invoice_update_session.period_start)
            return HttpResponse(
                                content=f'Profile located. Webhook received: { event["type"] }',
                                status=200
                                )
        else:
            return HttpResponse(
                    content=f'{invoice_update_session.customer_name}: User Profile could not be located',
                                status=500)

    def handle_invoice_paid(self, event):

        return HttpResponse(
                            content=f'Invoice Paid. Webhook Received: { event["type"] }',
                            status=200
                            )

    def handle_invoice_payment_failed(self, event):

        return HttpResponse(
                            content=f'Invoice Payment Failed. Webhook Received:{event["type"]}',
                            status=200
                            )

    def handle_subscription(self, event):

        subscription_object = event.data.object

        subscriber_profile, found_profile = process_user_profile(subscription_object)

        if found_profile:
            subscriber_profile.next_payment_date(subscription_object.current_period_end)
            subscriber_profile.last_payment_date(subscription_object.current_period_start)
            subscriber_profile.payment_start_date(subscription_object.billing_cycle_anchor)
            return HttpResponse(
                                content=f'Profile located. Webhook received: { event["type"] }',
                                status=200
                                )
        else:
            return HttpResponse(
                    content=f'{subscription_object.customer}: User Profile could not be located',
                                status=500)


def process_user_profile(stripe_session):
    '''
    Takes a stripe_session object, extracts relevant data
    Uses data to retrieve user_profile from db
    Returns a tuple of: user_profile, Boolean
    '''
    stripe_objects = ['checkout.session', 'invoice', 'intent',
                      'plan', 'subscription', 'payment_intent']

    if stripe_session.object not in stripe_objects:
        raise TypeError(f'Expected: Stripe object. Received: {stripe_session}')

    lookup_dict = {}

    print('Get Attr test - process_user_profile:' + str(getattr(stripe_session, 'customer')))

    if getattr(stripe_session, 'customer', None) is not None:
        lookup_dict['customer_id'] = stripe_session.customer
    if getattr(stripe_session, 'client_reference_id', None) is not None:
        lookup_dict['user_id'] = stripe_session.client_reference_id
    if getattr(stripe_session, 'customer_email', None) is not None:
        lookup_dict['stripe_email'] = stripe_session.customer_email

    sub_user_profile = None

    user_exists = False
    attempt = 1
    while attempt <= 5:
        try:
            sub_user_profile = Profile.objects.get(**lookup_dict)
            user_exists = True
            break
        except Profile.DoesNotExist:
            attempt += 1
            sleep(1)
    if user_exists:
        return sub_user_profile, True
    else:
        return None, False


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
    subscriber.groups.add(SubscriberGroup)
    print(f'Successfully Added {subscriber} to Subscriber Group')
    return subscriber.groups.all(), True








