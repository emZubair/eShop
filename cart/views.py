from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product
from coupons.forms import CouponApplyForm
from common.constants import KEY_QUANTITY


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product, quantity=cd.get('quantity'), override_quantity=cd.get('override'))
    return redirect('cart:cart_details')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)
    return redirect('cart:cart_details')


def cart_details(request):
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    for item in cart:
        item['product_update_form'] = CartAddProductForm(initial={
            KEY_QUANTITY: item.get(KEY_QUANTITY), 'override': True
        })
    return render(request, 'cart/cart_details.html', {'cart': cart,
                                                      'coupon_apply_form': coupon_apply_form})
