from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'telephone',
                  'address_1', 'address_2', 'address_3',
                  'town_city', 'country', 'post_code'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
                'full_name': 'Full Name',
                'email': 'Email Address',
                'telephone': 'Telephone Number',
                'country': 'Country',
                'post_code': 'Postal Code',
                'town_city': 'Town or City',
                'address_1': 'Address Line 1',
                'address_2': 'Address Line 2',
                'address_3': 'Address Line 3'
                }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{ placeholders[field] } *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
