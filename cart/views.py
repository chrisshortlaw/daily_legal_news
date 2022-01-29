from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from products.models import Product

# Create your views here.


def cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    '''
    Adds a product to a user's cart
    '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    product = Product.objects.get(id=product_id)

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    messages.success(request, f'Added {product.name}')

    request.session['cart'] = cart

    return redirect(redirect_url)


def modify_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    messages.success(request, f'Added {product.name}')

    request.session['cart'] = cart

    return redirect(reverse('cart'))


def remove_product(request, product_id):

    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)

    try:
        cart.pop(product_id)

        messages.success(request, f'Removed {product.name}')

        request.session['cart'] = cart
        return redirect(reverse('cart'))
    except Exception as e:
        messages.error(request, f'{e}')
        return HttpResponse(status=500)
