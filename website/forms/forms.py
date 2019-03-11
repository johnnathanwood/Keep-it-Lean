from django.contrib.auth.models import User
from django import forms
from website.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('UPC','description')

