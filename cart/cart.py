from decimal import Decimal

from django.conf import settings

from shop.models import Product
from common.constants import (KEY_PRICE, KEY_QUANTITY, KEY_PRODUCT, KEY_TOTAL_PRICE)


class Cart(object):

    def __init__(self, request):
        """
        initialize the cart
        :param request: (HttpRequest)
        """

        self.session = request.session
        cart = self.session.get(settings.SESSION_CART_ID)
        if not cart:
            cart = self.session[settings.SESSION_CART_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add Item in cart or update its quantity
        :param product:
        :param quantity:
        :param override_quantity:
        """

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                KEY_QUANTITY: 0, KEY_PRICE: str(product.price)
            }
        if override_quantity:
            self.cart[product_id][KEY_QUANTITY] = quantity
        else:
            self.cart[product_id][KEY_QUANTITY] += quantity
        self.save()

    def save(self):
        """
        Save marks the session as modified to make sure it gets saved
        """

        self.session.modified = True

    def remove(self, product):
        """
        remove product from the cart
        :param product:
        """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        iterate through the items in the cart to get the products from the DB
        """

        product_keys = self.cart.keys()

        products = Product.objects.filter(id__in=product_keys)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)][KEY_PRODUCT] = product

        for item in cart.values():
            item[KEY_PRICE] = Decimal(item[KEY_PRICE])
            item[KEY_TOTAL_PRICE] = item[KEY_PRICE] * item[KEY_QUANTITY]
            yield item

    def __len__(self):
        return sum([item[KEY_QUANTITY] for item in self.cart.values()])

    def get_total_price(self):
        return sum([Decimal(item[KEY_QUANTITY]) * Decimal(item[KEY_PRICE]) for item in self.cart.values()])

    def clear(self):
        del self.session[settings.SESSION_CART_ID]
