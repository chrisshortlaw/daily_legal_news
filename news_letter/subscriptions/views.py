from django.http.request import HttpRequest
from subscriptions.models import ServiceProduct, Subscription
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.models import User
from user_profiles.models import Profile

from django.contrib import messages

import stripe
# Create your views here.


# Subscription Page Views

def subscriptions(request):

    subscription_products = Subscription.objects.all()

    context = {
            'subscription_products': subscription_products,
            }

    return render(request, 'subscription.htmldjango', context=context)


def subscription_success(request):

    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    customer = stripe.Customer.retrieve(session.customer)
    print(f'Stripe Session: {session}')
    print(f'Customer: { customer }')

    try:

        subbed_user = User.objects.get(
                                       request.user.email['email']
                                        )
        subbed_profile = Profile.objects.get(user=subbed_user)
        if subbed_profile:
            subbed_profile.customer_id = customer.id
            subbed_profile.stripe_email = customer.email
            subbed_profile.stripe_name = customer.name
    except Exception as e:
        messages.error(request, f'Error: {e}. Please contact customer service')
        return redirect(reverse('index'))

    context = {
                'session': session,
                'customer': customer
            }

    return render(request, 'subscription_success.html', context=context)


def subscription_fail(request):
    return render(request, 'subscription_fail.html')


def create_checkout_session(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        price = request.POST['priceId']
        try:
            stripe.api_key = stripe_secret_key 

            checkout_session = stripe.checkout.Session.create(
                    success_url= 'http://localhost:8000/subscriptions/subscribe/success?session_id={CHECKOUT_SESSION_ID}',
                    #TODO Fix in deployment -,
                    cancel_url='http://localhost:8000/subscriptions/subscribe/fail',
                    mode='subscription',
                    line_items=[{
                                'price': price,
                                'quantity': 1
                                }],
                    )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect(reverse('subscriptions'))



