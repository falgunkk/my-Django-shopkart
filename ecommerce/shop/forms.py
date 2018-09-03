from django import forms

from .models import Category
categories = Category.objects.all()
categories_list = []
for category in categories:
	categories_list.append((category.id, category.name))


class ProductForm(forms.Form):
    category = forms.CharField(label='Category', widget=forms.Select(choices=categories_list))
    name = forms.CharField(label='name', max_length=150)
    price = forms.DecimalField(label='price', max_digits=10, decimal_places=2)
    available = forms.BooleanField(label='Available',required=False, initial=True)
    stock = forms.IntegerField(label='stock')
    description = forms.CharField(label='description', max_length=150)
    image = forms.ImageField(label='product image',required=False)
