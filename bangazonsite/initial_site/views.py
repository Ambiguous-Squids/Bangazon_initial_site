from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from . import models
from .models import User
from .forms import AddProductForm, AddPaymentTypeForm, UserForm, UserProfileForm

# class views

class productDetailView(DetailView):
    model = models.Product

class success(TemplateView):
    template = 'success.html'

# function views

def register(request):
    """
    View function to register a new user/customer.
    @asimonia
    """
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True
        else:
            # Invalid form or forms.  Print to terminal
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        

    return render(request, 'registration/register.html',
            {'user_form': user_form,
             'profile_form': profile_form,
             'registered': registered})


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
        'product_type': product_type[0]
    })

@login_required

def get_payment_type(request):
    new_cust = models.Customer.objects.filter(user = request.user)
    payments = models.PaymentType.objects.filter(customer = new_cust)
    return render(request, 'initial_site/payment_list.html',{
        'payment_list': payments,
        'user': request.user
    })


def add_product(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(redirect_to='/')
        else:
            print(form.errors)
    return render(request, 'initial_site/add_product.html', {'form': form})

@login_required
def add_payment_type(request):
    form = AddPaymentTypeForm()

    if request.method == 'POST':
        form = AddPaymentTypeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # Setting next so the django reroutes user to previous page
            next = request.POST.get('next', '/')
            # Redirect to previous page
            return HttpResponseRedirect(next)
        else:
            print(form.errors)
    return render(request, 'initial_site/add_payment_type.html', {'form': form})

def add_product_to_order(request):
    pass

def order_detail(request):
    pk = models.Order.objects.filter(customer = request.user.id, active = 1)
    active_order = models.Order.objects.filter(pk = pk)[0]
    products = active_order.products.all()
    payment_types = models.PaymentType.objects.filter(customer = request.user.id)
    total = 0

    for product in products:
        total += product.price

    if request.method == 'POST':
        payment = models.PaymentType.objects.filter(pk = request.POST['select_payment'])[0]
        active_order.payment_type = payment
        active_order.active = 0
        active_order.save()
        return render(request, 'initial_site/success.html', {'confirm_order': request.POST})
        # return HttpResponseRedirect(redirect_to='/success')

    else:
        return render(request, 'initial_site/order_detail.html', {
            'active_order': active_order,
            'products': products,
            'total': total,
            'payment_types': payment_types,
            'pk': pk
            })

