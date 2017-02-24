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



def get_products(request):
    products = models.Product.objects.order_by('product_type')
    departments = models.ProductType.objects.order_by('label')
    return render(request, 'initial_site/product_list.html', {
        'object_list': products,
        'departments_list': departments
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
