#! /usr/bin/env python3.6
# Python 3.6 or newer required.
import json

from django.conf import settings
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.web_hook_handler import StripeWebHookHandler

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51KL7FbDDAG3wj1f3ZLiRzdL8DIZKU6bmFI32OziXurA3jn0i5GVCMNFnhjkhekiZDefOoA16XzQs8h7hZp0TWBs800F622n5Xv'

# Replace this endpoint secret with your endpoint's unique secret
# If you are testing with the CLI, find the secret by running 'stripe listen'
# If you are using an endpoint defined with the API or dashboard, look in your webhook settings
# at https://dashboard.stripe.com/webhooks
endpoint_secret = 'whsec_...'

@require_POST
@csrf_exempt
def webhook(request):
    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except Exception as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return HttpResponse(content=e, status=400)
    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return HttpResponse(content=e, status=400)

    # Handle the event
    if event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        response = StripeWebHookHandler.handle_payment_intent_failed(payment_intent)
    elif event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        response = StripeWebHookHandler.handle_payment_intent_succeeded(payment_intent)
    # ... handle other event types
    else:
        print('Unhandled event type {}'.format(event['type']))

    return response
