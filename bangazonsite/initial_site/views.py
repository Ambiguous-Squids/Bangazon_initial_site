from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from initial_site import models

class ProductsView(ListView):
    model = models.Product

    def get_queryset(self):
        return models.Product.objects.all()


class AddProductsView(TemplateView):
    template_name = 'initial_site/add_products.html'



