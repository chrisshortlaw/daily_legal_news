from django.http import HttpResponse
from time import sleep

from .models import OrderLineItem, Order
from products.models import Product


class StripeWebHookHandler:
    '''
    Handles Stripe webhooks
    '''

    def __init__(self, request):
        self.request = request

    def handle_webhook(self, event):

        return HttpResponse(content=f'Webhook Received: {event["type"]}',
                            status=200)

    def handle_payment_intent_succeeded(self, event):
        '''
        Handle the payment.intent webhook from stripe
        '''
        intent = event.data.object
        pay_id = intent.id
        cart = intent.metadata.cart
        # save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        end_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        # Checks 5 times if Order is in system
        while attempt <= 5:
            try:
                order = Order.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        telephone__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_city__iexact=shipping_details.address.city,
                        address_1__iexact=shipping_details.address.line1,
                        address_2__iexact=shipping_details.address.line2,
                        address_3__iexact=shipping_details.address.line3,
                        order_total=end_total,
                        original_cart=cart,
                        stripe_payment_id=pay_id
                        )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                sleep(1)
        if order_exists:
            return HttpResponse(
                    content = f'Webhook recieved: { event["type"] } | SUCCESS: Verified order already in database',
                    status=200
                    )
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        telephone__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_city__iexact=shipping_details.address.city,
                        address_1__iexact=shipping_details.address.line1,
                        address_2__iexact=shipping_details.address.line2,
                        address_3__iexact=shipping_details.address.line3,
                        order_total=end_total,
                        original_cart=cart,
                        stripe_payment_id=pay_id
                )
                for item_id, item_data in cart.items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data
                                )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                        content=f'Webhook received: {event["type"]}|Error{e}',
                        status=500
                        )
            return HttpResponse(
                                content=f'Webhook Received: {event["type"]}|Success: Created order in webhook',
                                status=200
                                )

    def handle_payment_intent_failed(self, event):
        '''
        Handle the payment_intent.payment_failed webhook
        '''
        return HttpResponse(
                content=f'Webhook Received: {event["type"]}',
                status=200
                )
