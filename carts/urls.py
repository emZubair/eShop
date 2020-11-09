from django.urls import path
from carts.views import cart_add, cart_details, cart_remove

app_name = 'carts'

urlpatterns = [
    path('', cart_details, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
