from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms.widgets import NumberInput


class AddToCartForm(forms.FORM):
    quantity = forms.NumberInput(label='Quantity'
                                  min_value=1,
                                  max_value=20,
                                  validators=[
                                              MinValueValidator,
                                              MaxValueValidator
                                             ],
                                  widget=forms.NumberInput(
                                                           max_value=20,
                                                           min_value=1,)


                                 )

