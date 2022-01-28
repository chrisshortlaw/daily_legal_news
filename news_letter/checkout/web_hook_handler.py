from django.http import HttpResponse
from time import sleep

from .models import OrderLineItem, Order
from products.models import Product
from django.contrib.auth.models import User


class StripeWebHookHandler:
    '''
    Handles Stripe webhooks
    '''

    def __init__(self, request):
        self.request = request

    def handle_webhook(self, event):

        return HttpResponse(content=f'handle_webhook: Webhook Received: {event["type"]}',
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
                                content=f'Webhook received: {event["type"]}|Error{e}',
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

        return HttpResponse(
                content=f'Checkout Session Completed: Webhook Received: {event["type"]}',
                status=200
                )

    def handle_invoice_paid(self, event):

        return HttpResponse(
                            content=f'Invoice Paid. Webhook Received: { event["type"] }',
                            status=200
                            )

    def handle_invoice_payment_failed(self, event):

        return HttpResponse(
                            content=f'Invoice Payment Failed. Webhook Received: { event["type"] }',
                            status=200
                            )
