from django.shortcuts import render
from django.views.generic.list import ListView
from initial_site import models

class ProductsView(ListView):
    model = models.Product

    def get_queryset(self):
        return models.Product.objects.all()