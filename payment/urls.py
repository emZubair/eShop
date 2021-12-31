from django.urls import path

from .views import payment_done, payment_process, payment_cancelled

app_name = 'payment'


urlpatterns = [
    path('done/', payment_done, name='done'),
    path('process/', payment_process, name='process'),
    path('cancelled/', payment_cancelled, name='cancelled')
]
