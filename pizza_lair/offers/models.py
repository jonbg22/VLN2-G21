from django.db import models

# Create your models here.

class Offer(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    amountPizza = models.IntField()
    price = models.FloatField()
    imgLink = models.CharField(max_length=999)
