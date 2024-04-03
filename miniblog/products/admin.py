from django.contrib import admin

# Register your models here.

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','description')