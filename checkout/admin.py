from django.contrib import admin

from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    '''
    What the hell is an inline? Is it actually important?
    No. It just allows you to edit models on the same page.
    '''
    model = OrderLineItem
    readonly_fields = ('lineitem_subtotal',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_number',
              'order_total',
              'date',
              'full_name',
              'email',
              'telephone',
              'country',
              'post_code',
              'town_city',
              'address_1',
              'address_2',
              'address_3')
    list_display = ('order_number',
                    'date',
                    'full_name',
                    'order_total')
    ordering = ('-date',)
