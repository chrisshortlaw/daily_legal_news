from .models import Profile
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'customer_id', '_next_payment_date', '_last_payment_date', '_payment_start_date', 'subscription', 'subscription_billing_id', 'subscription_amount', 'stripe_name', 'stripe_email', 'subscription_status', 'is_subscriber')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'default_full_name': 'Full Name',
                'default_email': 'Email Address',
                'default_telephone': 'Telephone Number',
                'default_country': 'Country',
                'default_post_code': 'Postal Code',
                'default_town_city': 'Town or City',
                'default_address_1': 'Address Line 1',
                'default_address_2': 'Address Line 2',
                'default_address_3': 'Address Line 3'
                }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{ placeholders[field] } *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
