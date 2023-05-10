from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, default="/static/images/profile.svg")
    zip = models.IntegerField(max_length=9999)
    city = models.CharField(max_length=9999)
    country = CountryField(max_length=9999)
    street = models.CharField(max_length=9999)
    house_number = models.IntegerField()
