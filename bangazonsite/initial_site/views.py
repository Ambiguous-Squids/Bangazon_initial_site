from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from initial_site import models

def get_products(request):
    products = models.Product.objects.order_by('product_type')
    departments = models.ProductType.objects.order_by('label')

    return render(request, 'initial_site/product_list.html', {
        'object_list': products,
        'departments_list': departments
        })

class AddProductsView(TemplateView):
    template_name = 'initial_site/add_products.html'

class productDetailView(DetailView):
	model = models.Product
