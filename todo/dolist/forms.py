from django import forms

from dolist.models import Store, Category, Product


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
