from subscriptions.models import ServiceProduct, Price, Subscription, Subscriber
from django.contrib import admin

# Register your models here.

@admin.register(Price)
class PriceInline(admin.ModelAdmin):
    fields = ('price_id',
              'price',
              'interval',)

    list_display = ('price', 'price_id', 'interval',)

@admin.register(ServiceProduct)
class ServiceProductInline(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    fields = ('service',
              'price')

    list_display = ('service', 'price', )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    fields = ('user',
              'subscription',
              'is_active')
    list_display = ('user', 'subscription', 'is_active')
