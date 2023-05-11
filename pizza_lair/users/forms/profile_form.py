from django.forms import ModelForm, widgets
from users.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_number': widgets.TextInput(attrs={'class': 'form-control'})
        }