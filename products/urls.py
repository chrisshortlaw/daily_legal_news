from django.urls import path

from . import views
'''
    urlpatterns explained: path('can have no name')
    , views.[insert name of function in views.py here]
    name = [insert name found in Config class in apps.py]
'''
urlpatterns = [
        path('', views.all_products, name='products'),
        path('<product_id>',
             views.product_page,
             name='product_page')
        ]
