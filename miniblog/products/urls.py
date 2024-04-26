from django.urls import path
from products.views import (
    product_list,
    product_create,
    product_detail,
    product_delete,
    product_update
    )

urlpatterns = [
    path('',view=product_list, name="product_list"),
    path('create/',view=product_create,name="product_create"),
    path('detail/<int:id>/',view=product_detail,name="product_detail"),
    path('delete/<int:id>/',view=product_delete,name="product_delete"),
    path('update/<int:id>/',view=product_update,name="product_update"),
]