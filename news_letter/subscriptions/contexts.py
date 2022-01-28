from django.shortcuts import get_object_or_404
from subscriptions.models import ServiceProduct, Price, Subscription, Subscriber 


def subscription_content(request):
    '''
    Returns context dict which can be accessed
    by other apps. Will contain subscription, subscriber,
    and price id
    '''
    # Subscriptions are the marriage of a product with a price
    # Prices are a price_id, an amount in cent/pence, and an interval
    subscriptions = Subscription.objects.all()

    context = {
               'subscriptions': subscriptions
            } 
    return context
