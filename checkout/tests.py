from typing import Dict, List
import json
from django.test import TestCase
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings

from django.contrib.auth.models import User, Group
from user_profiles.models import Profile
from .web_hook_handler import process_user_profile, add_user_to_subscriber_group

import stripe
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

        stripe.api_key = settings.STRIPE_SECRET_KEY

        self.checkout_session = stripe.checkout.Session.retrieve('cs_test_a1yPeLKLyMBLnxN2gtuwdASMG6D5Ka283dLQXZv4Pj1XLeTBrHikiUvBqr')
        self.checkout_session_fail = stripe.checkout.Session.retrieve('cs_test_a1xGQLOPT0lZ4FUQtMoUDq2RcypVtuivWG6p8si1tlwKuiXgYSwDuPxF6T')
        self.stripe_test_user_failing_1 = User.objects.create_user(username='stripe_test_fail',
                                                              email='thisshouldfail@email.com',
                                                              password='testfail')
        self.stripe_test_user_failing_1.save()
        self.stripe_test_user_failing_1.profile.customer_id = 'fake_id'
        self.stripe_test_user_failing_1.profile.stripe_email = 'fake@email.com'
        self.stripe_test_user_failing_1.profile.save()

        self.new_group, created = Group.objects.get_or_create(name='Subscriber')

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

    def testProcessUserProfile(self):

        self.assertEqual(self.checkout_session.object, 'checkout.session')

        self.stripe_test_user_passing_1 = User.objects.create_user(username='stripe_test_user',
                                                                   email='iamtom@tom.com',
                                                                   password='testpass')
        self.stripe_test_user_passing_1.save()
        test_user_profile = self.stripe_test_user_passing_1.profile
        test_user_profile.customer_id = self.checkout_session.customer
        test_user_profile.stripe_email = self.checkout_session.customer_email
        test_user_profile.save()

        self.subscribing_user_profile = process_user_profile(self.checkout_session)

        self.assertIsInstance(self.subscribing_user_profile[0], Profile)
        self.assertTrue(self.subscribing_user_profile[1])
        self.assertEqual(self.subscribing_user_profile[0].customer_id,
                         self.stripe_test_user_passing_1.profile.customer_id)

        self.failing_user_profile = process_user_profile(self.checkout_session_fail)

        self.assertEqual(self.failing_user_profile[0], None)
        self.assertEqual(self.failing_user_profile[1], False)

    def testAddUserToSubscribers(self):

        new_subscriber = User.objects.create_user(username='test_sub',
                                                  email='test@email.com',
                                                  password='Testpass123')
        new_subscriber.save()
        self.assertIsInstance(new_subscriber.profile, Profile)

        sub_profile = new_subscriber.profile

        added_subscriber = add_user_to_subscriber_group(sub_profile)

        self.assertTrue(added_subscriber[0].exists())

        self.assertTrue(added_subscriber[1])

        subscriber_group = Group.objects.get(name='Subscriber')

        self.assertTrue(subscriber_group in added_subscriber[0])
