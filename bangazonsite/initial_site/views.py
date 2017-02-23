from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .models import User
from initial_site.forms import AddProductForm, AddPaymentTypeForm
# class views

class IndexView(TemplateView):
    template_name = 'initial_site/login.html'


class LoginSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'initial_site/home.html'


class Register(TemplateView):
    template_name = 'initial_site/register.html'


class productDetailView(DetailView):
    model = models.Product

# function views


def get_products(request):
    products = models.Product.objects.order_by('product_type')
    departments = models.ProductType.objects.order_by('label')
    return render(request, 'initial_site/product_list.html', {
        'object_list': products,
        'departments_list': departments
    })


def register_user(request):
    data = request.POST
    user = User.objects.create_user(
        username = data['username'],
        password = data['password'],
        email = data['email'],
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    return login_user(request)


def login_user(request):
    data = request.POST
    username = data['username']
    password = data['password']
    user = authenticate(
        username = username,
        password = password
    )
    if user is not None:
        login(request = request, user = user)
    else:
        return HttpResponseRedirect(redirect_to='/')
    return HttpResponseRedirect(redirect_to='/success')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')

def add_product(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return index(request)
        else:
            print(form.errors)
    return render(request, 'initial_site/add_product.html', {'form': form})

def add_payment_type(request):
    form = AddPaymentTypeForm()

    if request.method == 'POST':
        form = AddPaymentTypeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return index(request)
        else:
            print(form.errors)
    return render(request, 'initial_site/add_payment_type.html', {'form': form})
