from django import forms

from product.models import Product

class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()