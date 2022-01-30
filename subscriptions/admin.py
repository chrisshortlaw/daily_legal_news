from subscriptions.models import (ServiceProduct, Price,
                                  Subscription, SubscriptionProduct)
from django.contrib import admin

# Register your models here.


@admin.register(Price)
class Price(admin.ModelAdmin):
    model = Price


@admin.register(ServiceProduct)
class ServiceProduct(admin.ModelAdmin):
    model = ServiceProduct


@admin.register(SubscriptionProduct)
class SubscriptionProductAdmin(admin.ModelAdmin):
    model = SubscriptionProduct
    list_display = ('service', 'price')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription

    list_display = ('user', 'sub_product', 'subscription_status', 'sub_id')
