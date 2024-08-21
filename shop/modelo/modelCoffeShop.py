from django.db import models
from .modelProducts import Products
from .modelClient import Client

class CoffeShop(models.Model):
    name = models.CharField(max_length=150)
    direction = models.CharField(max_length=200)
    productos = models.ManyToManyField(Products)
    clientes = models.ManyToManyField(Client) 

    def __str__(self):
        return self.name