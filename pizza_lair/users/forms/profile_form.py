from django.forms import ModelForm, widgets
from users.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude =['id', 'user']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'})
        }