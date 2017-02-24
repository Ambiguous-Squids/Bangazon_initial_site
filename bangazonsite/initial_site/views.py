from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from . import models
from .models import User
from .forms import AddProductForm, AddPaymentTypeForm

# class views

class productDetailView(DetailView):
    model = models.Product

# function views

def index(request):
    """
    View function for the splash page of site.
    @asimonia
    """
    # Generate counts of some of the main objects
    num_product_types = models.ProductType.objects.all().count()
    num_products = models.Product.objects.all().count()

    return render(request, 'index.html', {
        'num_products':num_products,
        'num_product_types':num_product_types
    })

def get_product_types(request):
    departments = models.ProductType.objects.order_by('label')
    return render(request, 'initial_site/product_type_list.html', {
        'departments_list': departments
    })

def get_products_of_type(request, pk):
    product_type = models.ProductType.objects.filter(id=pk)
    products = models.Product.objects.filter(product_type=pk)
    return render(request, 'initial_site/product_list.html', {
        'product_list': products,
        'product_type': product_type
    })


def add_product(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(redirect_to='/success')
        else:
            print(form.errors)
    return render(request, 'initial_site/add_product.html', {'form': form})


def add_payment_type(request):
    form = AddPaymentTypeForm()

    if request.method == 'POST':
        form = AddPaymentTypeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(redirect_to='/success')
        else:
            print(form.errors)
    return render(request, 'initial_site/add_payment_type.html', {'form': form})
