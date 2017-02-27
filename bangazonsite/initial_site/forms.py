from django import forms
from initial_site.models import Product, PaymentType, Customer
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class AddProductForm(forms.ModelForm):
    description = forms.CharField(max_length=4000, help_text="Please enter the description of your product.")

    class Meta:
        model = Product
        help_texts = {
            'name': _('Please enter the name of your product.'),
            'product_type': _('Please choose a category'),
            'price': _('Please enter a price.'),
            'quantity': _('Please enter a quantity.')
        }
        fields = ('name', 'product_type', 'description', 'price', 'quantity')

class AddPaymentTypeForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        help_texts = {
            'payment_type_name': _('Please enter the type of card you would like to add.'),
            'first_name': _('Please enter your first name'),
            'last_name': _('Please enter your last name'),
            'account': _('Please enter the card number.'),
            'expiration_date': _('Please enter the expiration date.'),
            'ccv': _('Please enter the ccv code.')
        }
        fields = ('payment_type_name', 'first_name', 'last_name', 'account', 'expiration_date', 'ccv')

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
