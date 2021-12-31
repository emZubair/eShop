from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

from braintree import BraintreeGateway

from common.utils import serialize_decimal
from orders.models import Order

gateway = BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session['order_id']
    order = get_object_or_404(Order, id=order_id)
    total_price = order.get_total_cost()

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce', None)
        resource = gateway.transaction.sale({
            'amount': serialize_decimal(total_price),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if resource.is_success:
            order.paid = True
            order.braintree_id = resource.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')
    else:
        client_token = gateway.client_token.generate()
        return render(request, 'payment/process.html', {
            'order': order, 'client_token': client_token
        })


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_cancelled(request):
    return render(request, 'payment/cancelled.html')
