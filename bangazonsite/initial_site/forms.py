from django import forms
from initial_site.models import Product

class AddProductForm(forms.ModelForm):
    # customer = forms.ForeignKey(widget=forms.HiddenInput())
    name = forms.CharField(max_length=50, help_text="Please enter the name of your product.")
    # product_type = forms.ForeignKey(ProductType, on_delete=models.CASCADE)
    description = forms.CharField(max_length=4000, help_text="Please enter the description of your product.")
    price = forms.DecimalField(max_digits=15, decimal_places=2, help_text="Please enter the price of your product.")
    # quantity = forms.IntegerField(default=1, help_text="Please enter the quantity of your product.")

    class Meta:
        model = Product
        fields = ('customer', 'name', 'product_type', 'description', 'price', 'quantity')
