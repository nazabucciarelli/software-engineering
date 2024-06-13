# Create your views here.

from django.shortcuts import (
    render,
    redirect)
from products.repository.product import ProductRepository

repository = ProductRepository()

def product_list(request):
    products = repository.get_all()
    return render(
        request,
        'product/list.html',
        dict(
            products = products
        )
    )

def product_create(request):

def product_detail(request,id):
    product = repository.get_by_id(id=id)
    return render(request,'product/detail.html',{'product':product})

def product_delete(request,id):
    repository.delete_product(id)
    return redirect('product_list')

def product_update(request):
    ...