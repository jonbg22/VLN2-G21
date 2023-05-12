from django.db import models
from menu.models import Pizza

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


class PizzaOfTheDay(models.Model):
    day = models.SmallIntegerField()
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)


