from django.test import TestCase
from .models import Customer, Product


class CustomerTest(TestCase):
	def test_is_a_customer(self):

		david = Customer("123 Front St", "456 Back St","Smyrna", "Tennssee", "37167")
		self.assertIsInstance(david, Customer)


class TestAddProduct(TestCase):
    """
    Author:
        @nchemsak
    """
    def test_add_a_product(self):
        uselessMachine = Product('UselessMachine', 39.99, 5)
        self.assertIsInstance(uselessMachine, Product)

