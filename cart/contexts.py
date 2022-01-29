
# Function to manage context for shopping cart

from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal


def cart_content(request):
    '''
    Returns context dict which can be
    accessed via any app in the project
    Add this function to the context
    processors in settings.py in project folder
    '''
    cart_content = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        sub_total = quantity * product.price
        total += quantity * product.price
        product_count += quantity
        cart_content.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'sub_total': sub_total
            })

    context = {
            "cart_content": cart_content,
            "total": total,
            "product_count": product_count
            }
    return context


