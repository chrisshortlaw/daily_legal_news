from django import forms


class SubscriptionForm(forms.Form):
     email = forms.EmailField()
     name = forms.CharField(max_length=50)


