from django.forms import ModelForm, widgets
from users.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude =['id', 'users']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }