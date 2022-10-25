from django import forms
from .models import Company, Product


class CreateCompanyForm(forms.ModelForm):


    class Meta:
        model = Company
        fields = ('company_name', 'company_description')

class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'product_price', 'product_description')