from django.forms import ModelForm, widgets
from users.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

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

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=5, max_length=150, widget=forms.TextInput({'class': 'form-control'})),
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput({'class': 'form-control'})),
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput({'class': 'form-control'}))
