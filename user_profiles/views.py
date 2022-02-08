from django.shortcuts import get_object_or_404, render

from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from subscriptions.models import Subscription
from article_page.models import Comment
# Create your views here.


@login_required
def profile(request):

    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm()
    subscription = {}

    if profile:
        user = profile.user
        try:
            subscription_obj = Subscription.objects.get(user=user)

            subscription['sub_type'] = subscription_obj.sub_product.service
            subscription['sub_start'] = subscription_obj.payment_start_date
            subscription['sub_prev'] = subscription_obj.last_payment_date
            subscription['sub_next'] = subscription_obj.next_payment_date
            subscription['sub_status'] = subscription_obj.get_subscription_status_display()
            subscription['sub_id'] = subscription_obj.sub_id
            subscription['sub_amount'] = int(subscription_obj.sub_product.price.price)/100

        except Subscription.DoesNotExist:
            pass

    comments = Comment.objects.filter(user=request.user)

    context = {
               "form": form,
               "profile": profile,
               "subscription": subscription,
               "comments": comments,
                }

    return render(request, 'profile.html', context=context)
