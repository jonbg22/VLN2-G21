from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.FloatField()
    imgLink = models.CharField(max_length=255)


class PizzaCategory(models.Model):
    name = models.CharField(max_length=255)


class ToppingCategory(models.Model):
    name = models.CharField(max_length=255)


class Topping(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ToppingCategory, on_delete=models.CASCADE)


class Pizza(models.Model):
    prodID = models.OneToOneField(Product, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    category = models.ManyToManyField(PizzaCategory)


class Side(models.Model):
    prodID = models.OneToOneField(Product, on_delete=models.CASCADE)


class Drink(models.Model):
    prodID = models.OneToOneField(Product, on_delete=models.CASCADE)

