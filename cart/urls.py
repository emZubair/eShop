from django.urls import path

from .views import cart_add, cart_remove, cart_details

app_name = 'cart'


urlpatterns = [
    path('', cart_details, name='cart_details'),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart_remove/<int:product_id>/', cart_remove, name='cart_remove')
]
