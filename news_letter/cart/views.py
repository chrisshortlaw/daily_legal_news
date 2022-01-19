from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse

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

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def modify_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart

    return redirect(reverse('cart'))


def remove_product(request, product_id):

    cart = request.session.get('cart', {})

    try:
        cart.pop(product_id)
        request.session['cart'] = cart
        return redirect(reverse('cart'))
    except Exception as e:
        return HttpResponse(status=500)





