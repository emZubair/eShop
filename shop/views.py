from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'category': category, 'categories': categories, 'products': products
    })


def product_details(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug, available=True)
    cart_add_form = CartAddProductForm()

    return render(request, 'shop/product/details.html', {
        'product': product, 'cart_add_form': cart_add_form
    })


