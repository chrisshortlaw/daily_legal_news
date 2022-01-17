
# Function to manage context for shopping cart

def add_to_cart(request):
    '''
    Returns context dict which can be
    accessed via any app in the project
    Add this function to the context
    processors in settings.py in project folder
    '''
    cart_content = []
    total = 0
    product_count = 0

    context = {
            "cart_content": cart_content,
            "total": total,
            "product_count": product_count
            }
    return context
