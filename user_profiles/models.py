from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from subscriptions.models import Subscription

# Create your models here.
SUBSCRIPTION_STATUS = [
        ('active', 'Current'),
        ('past_due', 'Past Due'),
        ('canceled', 'Cancelled'),
        ('none', 'None'),
        ('incomplete', 'Incomplete'),
        ('incomplete_expired', 'Incomplete Expired'),
        ('trialing', 'Trialing'),
        ('unpaid', 'Unpaid')
        ]


class Profile(models.Model):
    '''
    Class for holding user profile information
    Fields:
        - user: Type[User] - OnetoOne
        - default_full_name
        - default_email
        - default_telephone
        - default_country
        - default_post_code
        - default_town_city
        - default_address_1
        - default_address_2
        - default_address_3
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    default_full_name = models.CharField(max_length=60, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_telephone = models.CharField(max_length=25, null=True, blank=True)
    default_country = models.CharField(max_length=30, null=True, blank=True)
    default_post_code = models.CharField(max_length=20, null=True, blank=True)
    default_town_city = models.CharField(max_length=30, null=True, blank=True)
    default_address_1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_2 = models.CharField(max_length=80, null=True, blank=True)
    default_address_3 = models.CharField(max_length=80, null=True, blank=True)
    customer_id = models.CharField(max_length=50, null=True, blank=True)
    stripe_email = models.EmailField(max_length=254, null=True, blank=True)
    stripe_name = models.CharField(max_length=50, null=True, blank=True)
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE,
                                     related_name='subscription',
                                     blank=True,
                                     null=True)
    is_subscriber = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    Create or update user profile when user is created or updated
    '''
    if created:

        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()
