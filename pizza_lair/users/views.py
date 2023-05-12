from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms.profile_form import ProfileForm, SignUpForm



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    form = SignUpForm()
    return render(request, 'users/register.html', {
        'form': form
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'users/profile.html', {
        'form': ProfileForm(instance=profile)
    })
