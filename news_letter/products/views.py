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
