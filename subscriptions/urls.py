from django.urls import path

from . import views

urlpatterns = [
        path('', views.subscriptions, name='subscriptions'),
        path('subscribe/',
             views.create_checkout_session,
             name='subscription_checkout'),
        path('subscribe/success',
             views.subscription_success,
             name="subscription_success"),
        path('subscribe/fail',
             views.subscription_fail,
             name="subscription_fail"),
        path('subscribe/cancel',
             views.cancel_subscription,
             name="subscription_cancel")
        ]
