from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.test.utils import setup_test_environment
from initial_site import models

'''
Unit Tests for the views
'''

setup_test_environment()

class ProductViewTests(TestCase):

    '''
    This class will test the views relating to Products
    '''

    def test_can_list_all_products(self):
        """
        Testing if we can list all products on a view
        """
        ball = models.Product("1", "1", 2, "Baseball", 33.33, 444)
        ball.save()
        
        client = Client()
        response = client.get(reverse('initial_site:products'))
        
        self.assertQuerysetEqual(response.context['object_list'], ['<Product: Baseball>'])


class CustomerTest(TestCase):
	def test_is_a_customer(self):

		david = models.Customer("123 Front St", "456 Back St","Smyrna", "Tennssee", "37167")
		self.assertIsInstance(david, models.Customer)


class TestAddProduct(TestCase):
    """
    Author:
        @nchemsak
    """
    def test_add_a_product(self):
        uselessMachine = models.Product('UselessMachine', 39.99, 5)
        self.assertIsInstance(uselessMachine, models.Product)
