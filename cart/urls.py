from django.urls import path

from . import views

urlpatterns = [
        path('', views.cart, name='cart'),
        path('add/<product_id>/', views.add_to_cart, name="add_to_cart"),
        path('modify/<product_id>', views.modify_cart, name="modify_cart"),
        path('remove/<product_id>/',
             views.remove_product,
             name="remove_product")
        ]
