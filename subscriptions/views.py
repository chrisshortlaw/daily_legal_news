from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user_profiles.models import Profile
from .models import Subscription, SubscriptionProduct
from checkout.web_hook_handler import remove_user_from_subscriber_group, add_user_to_subscriber_group

import stripe
# Create your views here.

# Subscription Page Views


def subscriptions(request):
    products = []
    subscription_products = SubscriptionProduct.objects.all()
    for product in subscription_products:
        prod_dict = {}
        sub_price = int(int(product.price.price) / 100)
        prod_dict['product'] = product
        prod_dict['sub_price'] = sub_price
        details = product.service.details.split(',')
        prod_dict['details'] = details
        products.append(prod_dict)


    context = {
            'subscription_products': products

            }

    return render(request,
                  'subscription.htmldjango',
                  context=context)


def subscription_success(request):

    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    customer = stripe.Customer.retrieve(session.customer)

    payment_amount = int(int(session.amount_total)/100)
    service = session.metadata.service

    try:
        subbed_user = User.objects.get(
                                       email=session.metadata.user_email
                                        )
        sub_product = SubscriptionProduct.objects.get(id=session.metadata.product_id)

        subbed_profile = Profile.objects.get(user__id=subbed_user.id)
        user_sub = Subscription.objects.filter(sub_id=session.subscription)

        if subbed_profile:
            subbed_profile.customer_id = customer.id
            subbed_profile.stripe_email = customer.email
            subbed_profile.stripe_name = customer.name
            subbed_profile.save()
        # add user to subscriber group
        add_user_to_subscriber_group(subbed_profile)


        if not user_sub:
            sub_product = SubscriptionProduct.objects.get(id=session.metadata.product_id)
            new_sub = Subscription(sub_product=sub_product,
                                   sub_id=session.subscription,
                                   user=subbed_profile.user,
                                   subscription_status='active')
            new_sub.save()
            messages.info(request, f'New Subscription Created for {subbed_profile.user}')
        else:
            sub_product = SubscriptionProduct.objects.get(id=session.metadata.product_id)
            # This is dangerous but should only return 1 object
            user_sub[0].sub_product.add(sub_product)
            user_sub[0].save()
            messages.info(request, f'Subscription details updated for {subbed_profile.user.email}')

    except Exception as e:
        messages.error(request,
                       f'Error: {e}. Please contact customer service')
        return redirect(reverse('index'))
    context = {
                'session': session,
                'customer': customer,
                'payment_amount': payment_amount,
                'service': service
                }

    return render(request,
                  'subscription_success.html',
                  context=context)


def subscription_fail(request):
    return render(request, 'subscription_fail.html')


@login_required
def create_checkout_session(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        price = request.POST['priceId']
        service = request.POST['serviceId']
        product_id = request.POST['productId']
        try:
            stripe.api_key = stripe_secret_key 

            user_ref = request.user.id
            user_email = request.user.email
            user_profile = Profile.objects.get(user=request.user)
            cust_id = user_profile.customer_id

            checkout_session = stripe.checkout.Session.create(
                    success_url= 'http://localhost:8000/subscriptions/subscribe/success?session_id={CHECKOUT_SESSION_ID}',
                    #TODO Fix in deployment -,
                    cancel_url='http://localhost:8000/subscriptions/subscribe/fail',
                    mode='subscription',
                    line_items=[{
                                'price': price,
                                'quantity': 1
                                }],
                    client_reference_id=user_ref,
                    customer_email=user_email,
                    metadata={
                        "product_id": product_id,
                        "price": price,
                        "service": service,
                        "user_email": user_email
                        }
                    )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect(reverse('subscriptions'))


@login_required
def cancel_subscription(request):

    if request.POST:
        user = User.objects.get(id=request.user.id)

        subscription = request.POST['subId']
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.Subscription.delete(
            subscription,
            )
        remove_user_from_subscriber_group(user)
        user.save()

        sub = Subscription.objects.get(sub_id=subscription)
        sub.subscription_status = 'canceled'
        sub.next_payment_date = None
        sub.sub_product = ""
        sub.save()
        messages.info(request, 'You have cancelled your subscription')
        return redirect(reverse('index'))
