from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50, required=True)
    card_number = CardNumberField(required=True)
    expiry_date = CardExpiryField(required=True)
    card_code = SecurityCodeField(required=True)
