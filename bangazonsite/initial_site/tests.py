from django.test import TestCase
from initial_site import models
from django.core.urlresolvers import reverse


class ProductDetailsViewTest(TestCase):

    def test_view_product_detail(self):

        walkman = models.Product('Walkman', {'product_id':1, 'product_type':'electronics'})
        walkman.save()

        # resp = self.client.get(reverse('product'), 'products/electronics/1')
        resp = self.client.get(reverse('product'), kwargs={'poll_id':1, 'product_type':'electronics'})
        
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['product'].product_id, 1)
        self.assertEqual(resp.context['product'].product_type, 'electronics')        

        # Non-existent products throw a 404.
        self.assertEqual(resp.status_code, 404)