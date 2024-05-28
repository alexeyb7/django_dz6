from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name', 'prod_desc', 'prod_price', 'prod_quant', 'photo']