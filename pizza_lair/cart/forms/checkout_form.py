from django.forms import ModelForm, widgets
from users.models import Profile

class CheckoutForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'name', 'profile_image']
        widgets = {
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'})
        }