from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50, required=True)
    card_number = forms.IntegerField(max_length=16, min_length=16, required=True)
    expiry_date = CardExpiryField(required=True)
    cvc = SecurityCodeField(required=True)
