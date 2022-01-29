from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import Product
from django.contrib import messages

# Create your views here.


def all_products(request):
    '''Displays all products'''
    products = Product.objects.all()
    query = None

    if 'search' in request.GET:
        query = request.GET['search']
        if not query:
            messages.error(request, "No search criteria specified.")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = Product.objects.filter(queries)

    context = {
            "Product": products,
            }

    return render(request, 'products/product.htmldjango', context)


def product_page(request, product_id):

    product = Product.objects.get(id=product_id)

    context = {"Product": product}

    return render(request, 'products/product_page.htmldjango', context)
