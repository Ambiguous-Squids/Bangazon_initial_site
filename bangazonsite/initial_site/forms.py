from django import forms
from initial_site.models import Product, PaymentType, Customer
from django.contrib.auth.models import User


class AddProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter the name of your product.")
    description = forms.CharField(max_length=4000, help_text="Please enter the description of your product.")
    price = forms.DecimalField(max_digits=15, decimal_places=2, help_text="Please enter the price of your product.")

    class Meta:
        model = Product
        fields = ('customer', 'name', 'product_type', 'description', 'price', 'quantity')

class AddPaymentTypeForm(forms.ModelForm):
    payment_type_name = forms.CharField(max_length=16,help_text="Please enter the type of card you would like to add.")
    first_name = forms.CharField(max_length=50,help_text="Please your first name")
    last_name = forms.CharField(max_length=50,help_text="Please your last name")
    account = forms.CharField(max_length=16,help_text="Please enter the card number.")
    expiration_date = forms.DateField(help_text= "Please enter the expiration date.")
    ccv = forms.CharField(max_length=3,help_text="Please enter the ccv code.")


    class Meta:
        model = PaymentType
        fields = ('customer','payment_type_name', 'first_name', 'last_name', 'account', 'expiration_date', 'ccv')

class UserForm(forms.ModelForm):
    """
    Form to register a new user.
    @asimonia
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    """
    Form to complete a customer profile.
    @asimonia
    """

    class Meta:
        model = Customer
        fields = ('address_1', 'address_2', 'city', 'state', 'zip_code')
