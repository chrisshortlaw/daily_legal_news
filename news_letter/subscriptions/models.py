from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ServiceProduct(models.Model):
    name = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Price(models.Model):
    price_id = models.CharField(max_length=50)
    price = models.IntegerField(default=0)  # Stripe requires cent/pence
    interval = models.CharField(max_length=30, default="month")

    def get_price(self):
        return f'€{ self.price }'

    def __str__(self):
        return f'{self.price} cent per { self.interval }'


class Subscription(models.Model):
    service = models.ForeignKey('ServiceProduct', on_delete=models.CASCADE)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.service.name}:{self.price.price}'

