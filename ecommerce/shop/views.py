from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from shop.forms import ProductForm
from django.template.defaultfilters import slugify


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    data = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)

def add_product(request):
    product_instance = Product()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_instance.category = Category.objects.get(id=form.data['category'])
            product_instance.name = form.data['name']
            product_instance.price = form.data['price']
            if form.data.__contains__('available'):
              product_instance.available = bool(form.data['available'])
            else:
              product_instance.available = False
            product_instance.stock = form.data['stock']
            product_instance.description = form.data['description']
            product_instance.image = form.data['image']
            product_instance.slug = slugify(form.data['name'])
            product_instance.save()
    else:
        form = ProductForm()
    return render(request, 'shop/product/add_product.html', {'form': form})