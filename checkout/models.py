import random
import string

from django.db import models
from django.db.models import Sum
from django.db.models.deletion import SET_NULL

from products.models import Product
from user_profiles.models import Profile

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=16, null=False, editable=False)
    user_profile = models.ForeignKey(Profile,
                                     on_delete=SET_NULL,
                                     related_name='orders',
                                     null=True,
                                     blank=True)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    telephone = models.CharField(max_length=25, null=True, blank=True)
    country = models.CharField(max_length=30, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    town_city = models.CharField(max_length=30, null=False, blank=False)
    address_1 = models.CharField(max_length=80, null=False, blank=False)
    address_2 = models.CharField(max_length=80, null=True, blank=True)
    address_3 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    original_cart = models.TextField(null=False,
                                     blank=False,
                                     default='')
    stripe_payment_id = models.CharField(max_length=254,
                                         null=False,
                                         blank=False,
                                         default='')
    order_total = models.DecimalField(decimal_places=2,
                                      max_digits=10,
                                      null=False,
                                      default=0)

    def _generate_unique_id(self, id_length):
        '''
        Uses Random.choices to generate a string of letters and digits
        of length id_length

        '''
        return ''.join(random.choices(string.ascii_uppercase + string.digits,
                                      k=id_length))

    def calculate_order_total(self):

        self.order_total = self.line_item.aggregate(Sum('lineitem_subtotal'))['lineitem_subtotal__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_unique_id(9)

        super().save(*args, **kwargs)

    def __str__(self):
        '''
        str method required for friendly name in admin screen
        '''
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              null=False,
                              on_delete=models.CASCADE,
                              related_name='line_item')
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_subtotal = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        """
        Set lineitem_subtotal
        """
        self.lineitem_subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} in order: {self.order.order_number}'
