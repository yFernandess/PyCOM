from django import forms

from produto.models import Produto

class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        exclude = ()