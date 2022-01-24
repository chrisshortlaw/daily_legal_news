from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Order, OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.calculate_order_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, created, **kwargs):

    instance.order.calculate_order_total()
