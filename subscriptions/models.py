from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class ServiceProduct(models.Model):
    name = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    price_id = models.CharField(max_length=50)
    price = models.IntegerField(default=0)  # Stripe requires cent/pence
    interval = models.CharField(max_length=30, default="month")

    def get_details(self):
        return f'€{ self.price } cent per { self.interval }'

    def __str__(self):
        return f'{self.price}'


class SubscriptionProduct(models.Model):
    service = models.ForeignKey('ServiceProduct',
                                on_delete=models.CASCADE,
                                related_name='service')
    price = models.ForeignKey('Price',
                              on_delete=models.CASCADE,
                              related_name="sub_price")

    def __str__(self):
        return f'{self.service}: { self.price }'


class Subscription(models.Model):
    SUBSCRIPTION_STATUS = [
            ('active', 'Active'),
            ('past_due', 'Past Due'),
            ('canceled', 'Cancelled'),
            ('none', 'None'),
            ('incomplete', 'Incomplete'),
            ('incomplete_expired', 'Incomplete Expired'),
            ('trialing', 'Trialing'),
            ('unpaid', 'Unpaid')
            ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscriber',
                             null=True, blank=True)
    sub_product = models.ForeignKey('SubscriptionProduct',
                                    on_delete=models.CASCADE,
                                    related_name="sub",
                                    null=True, blank=True)
    sub_id = models.CharField(max_length=50,
                              default='missing_id')
    subscription_status = models.CharField(max_length=25,
                                           choices=SUBSCRIPTION_STATUS,
                                           default='incomplete')
    _payment_start_date = models.DateField(null=True, blank=True)
    _next_payment_date = models.DateField(null=True, blank=True)
    _last_payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.sub_product}:{self.sub_id}'

    @property
    def payment_start_date(self):
        if self._payment_start_date is not None:
            return self._payment_start_date

    def set_payment_start_date(self, timestamp):
        self._payment_start_date = datetime.datetime.fromtimestamp(timestamp).date()
        return self._payment_start_date

    @property
    def next_payment_date(self):
        if self._next_payment_date is not None:
            return self._next_payment_date

    def set_next_payment_date(self, timestamp):
        self._next_payment_date = datetime.datetime.fromtimestamp(timestamp).date()

    @property
    def last_payment_date(self):
        if self._last_payment_date is not None:
            return self._last_payment_date

    def set_last_payment_date(self, timestamp):
        self._last_payment_date = datetime.datetime.fromtimestamp(timestamp).date()
        return self._last_payment_date
