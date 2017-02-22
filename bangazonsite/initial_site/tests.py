from django.test import TestCase
from .models import Customer
# Create your tests here.

class CustomerTest(TestCase):
	def test_is_a_customer(self):
		
		david = Customer("123 Front St", "456 Back St","Smyrna", "Tennssee", "37167")
		self.assertIsInstance(david, Customer)