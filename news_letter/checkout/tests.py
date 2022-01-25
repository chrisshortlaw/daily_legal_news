from typing import Dict
from django.test import TestCase
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from django.shortcuts import get_object_or_404

# Create your tests here.


class TestCheckout(TestCase):

    def setUp(self) -> None:
        '''
        Sets up the OrderForm, the Product, and the cart 
        which will be used to test the logic of the checkout models
        '''

        self.form_data = {
                'full_name': 'Test Name',
                'email': 'test@testmail.com',
                'telephone': '001 555 9000',
                'country': 'Ireland',
                'post_code': '95030',
                'town_city': 'Test City',
                'address_1': 'Test Apartment',
                'address_2': 'Test Block',
                'address_3': 'Test Street'
                }

        self.order_form = OrderForm(self.form_data)
# Set up Product
        new_product = Product(name='test_Product',
                              description='A test product',
                              price=1.00,
                              )
        new_product.save()
# Set up cart and add product
        product = Product.objects.get(name="test_Product")
        product_id = product.id

        quantity = 1
        cart = {}

        cart[product_id] = quantity
        self.cart = cart

# Set Up Context
        sub_total = 0
        cart_content = []
        product_count = 0
        total = 0

        for product_id, quantity in self.cart.items():
            product = get_object_or_404(Product, id=int(product_id))
            sub_total = quantity * product.price
            total += quantity * product.price
            product_count += quantity
            cart_content.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
                'sub_total': sub_total
                })

        self.context = {'cart_content': cart_content,
                        'total': total,
                        'product_count': product_count
                        }

        self.order = self.order_form.save()

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def testOrderForm(self):
        self.assertIsInstance(self.order_form, OrderForm)
        self.assertNotIsInstance(self.order_form, Order)

        self.assertTrue(self.order_form.is_valid(), 'order_form is not valid')

        self.assertIsInstance(self.order, Order)
        self.assertIsNotNone(self.order.order_number)
        self.assertTrue(self.order.order_total == 0)

    def testOrderLineItem(self):

        self.assertTrue(len(self.cart.items()) == 1)
        self.assertIsInstance(self.cart, Dict)

        for item_id, item_data in self.cart.items():
            try:
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                            order=self.order,
                            product=product,
                            quantity=item_data
                            )
                    order_line_item.save()
                else:
                    pass
            except Product.DoesNotExist:
                pass

        order_line_items = OrderLineItem.objects.all()

        self.assertTrue(len(order_line_items) == 1,
                        'Error: Length of order_line_items is greater than 1. Expected: 1')

        self.assertIsInstance(order_line_items[0].order, Order)
        self.assertIsInstance(order_line_items[0].product, Product)

# Check if self.order has updated with addition of line item
        self.assertTrue(self.order.order_total == 1.00)
        # self.assertIsInstance(self.order.date, Date)
