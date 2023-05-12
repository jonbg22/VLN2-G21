from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from django.core.validators import RegexValidator

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50, required=True)
    card_number = forms.CharField(required=True, min_length=16, max_length=16, validators=[RegexValidator("^(?:-(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))|(?:0|(?:[1-9](?:\\d{0,2}(?:,\\d{3})+|\\d*))))(?:.\\d+|)$")])
    expiry_date = CardExpiryField(required=True)
    cvc = SecurityCodeField(required=True)
