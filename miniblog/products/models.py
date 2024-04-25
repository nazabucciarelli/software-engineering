from django.contrib import admin
from django.db import models
from categories.models import Category
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null=True, blank=True
    )
    stock = models.IntegerField(default=0)

    @admin.display(description="Rango de precios")
    def get_price_range(self):
        if self.price > 1000000:
            return "Alto"
        if 500000 < self.price < 1000000:
            return "Medio"
        else:
            return "Bajo"
        

    def __str__(self):
        return self.name