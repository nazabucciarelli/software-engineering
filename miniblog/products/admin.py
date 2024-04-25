from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('-name','-price') # para que se ordenen por defecto las listas
    search_fields = ('name','category__name') # Es para que cuando buscamos en el search bar, busquemos por estos dos parametros
    empty_value_display = "Aun no tiene valor"
    list_filter = ("category",)
    list_editable = ('price',) # Convierte el campo en editable
    
    list_display = ('name','price','description','category','get_price_range','get_total','get_stock')
    readonly_fields = ('name',)
    fieldsets = [
        (
            "Información del producto",
            {
                "fields": ['name','price'],
            }
        ),
        (
            "Mas info del producto",
            {
                "classes":['collapse'],
                "fields": ['description','stock'],
            }
        )
    ]

    def get_total(self, obj):
        return obj.price * obj.stock
    
    def get_stock(self,obj):
        POCO = '#FF0000'
        MUCHO = '#008000'
        ESCASO = '#FFD300'
        codigo = ESCASO
        if obj.stock < 10:
            codigo = POCO
        elif obj.stock > 300:
            codigo = MUCHO
        return format_html(
            '<span style="color: {}">{}</span>',
            codigo,obj.stock
        )