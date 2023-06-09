from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.FloatField()
    imgLink = models.CharField(max_length=999)


class PizzaCategory(models.Model):
    name = models.CharField(max_length=255)


class ToppingCategory(models.Model):
    name = models.CharField(max_length=255)


class Topping(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ToppingCategory, on_delete=models.CASCADE)


class Pizza(models.Model):
    prod = models.OneToOneField(Product, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    category = models.ManyToManyField(PizzaCategory)

    def __str__(self):
        return str(self.prod.name)



class Side(models.Model):
    prod = models.OneToOneField(Product, on_delete=models.CASCADE)


class Drink(models.Model):
    prod = models.OneToOneField(Product, on_delete=models.CASCADE)

