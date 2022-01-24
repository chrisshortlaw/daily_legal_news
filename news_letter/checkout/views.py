import json

from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_content
from django.conf import settings
from products.models import Product
from djanog.http import require_POST

import stripe

# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:    
        pay_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pay_id, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            # 'save_info': request.POST.get('save_info'),
            'username': request.user,

            })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Error: Sorry, your payment was not processed.')


def check_out(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data
                                )
                        order_line_item.save()
                    else:
                        pass
                except Product.DoesNotExist:
                    messages.error(request,
                                   ('Error. {{ item_id }} was not found in database. Please contact customer support at (+353) 555 000')
                                   )
                    return redirect(reverse(('cart')))
                return redirect(reverse('checkout_success',
                                        args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form')
    else:

        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, 'Your cart is empty.')
            return redirect(reverse('products'))

        current_cart = cart_content(request)
        total = current_cart['total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency='eur',
                )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing')

        context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret
                }
        return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):

    save_info = request.session.get('save_info')

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order Success. Number: {order_number}')

    if 'cart' in request.session:
        del request.session['cart']

    context = {"order": order}

    return render(request, 'checkout/checkout_success.html', context=context)
