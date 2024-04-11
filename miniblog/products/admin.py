from django.contrib import admin

# Register your models here.

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('-name','-price') # para que se ordenen por defecto las listas
    search_fields = ('name','category__name') # Es para que cuando buscamos en el search bar, busquemos por estos dos parametros
    empty_value_display = "Aun no tiene valor"
    list_filter = ("category",)
    list_editable = ('price',) # Convierte el campo en editable
    
    list_display = ('name','price','description','category')