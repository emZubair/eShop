from celery import task

from django.core.mail import send_mail

from orders.models import Order
from common.utils import log_info
from cart.cart import Cart


@task
def order_created(order_id):

    order = Order.objects.get(id=order_id)
    subject = f"Dear {order.first_name}, Order :{order.id} placed"
    message = f"Order ID: {order.id} \nKeep ${order.get_total_cost()} to collect your order"
    log_info(f'Sending email to :{order.email}')
    return send_mail(subject, message, from_email=order.email, recipient_list=[order.email])

