from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    '''Displays all products'''

    products = Product.objects.all()

    context = {
            "Product": products,
            }

    return render(request, 'products/product.htmldjango', context)


def product_page(request, product_name):

    product = Product.objects.get(name=str(product_name))

    context = {"Product": product}

    return render(request, 'products/product_page.htmldjango', context)
