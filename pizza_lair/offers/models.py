from django.db import models

# Create your models here.

class Offer(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    amountPizza = models.IntegerField()
    amountSides = models.IntegerField()
    amountDrinks = models.IntegerField()
    price = models.FloatField()
    pickup = models.BooleanField()
    imgLink = models.CharField(max_length=999)

