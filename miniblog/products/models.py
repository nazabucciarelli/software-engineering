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

    def __str__(self):
        return self.name