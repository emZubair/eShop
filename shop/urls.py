from django.urls import path

from .views import product_list, product_details


app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:product_id>/<slug:product_slug>/', product_details, name='product_details'),
]
