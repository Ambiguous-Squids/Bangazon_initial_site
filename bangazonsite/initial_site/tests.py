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
        response = client.get(reverse('products'))
        
        self.assertQuerysetEqual(response.context['object_list'], ['<Product: Baseball>'])
