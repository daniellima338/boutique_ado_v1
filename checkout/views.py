from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))
    

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K8liwIYUGDUWOKhUzBnlWpxmT4QiqPlqHrr54UjjpMjIgWNzl2hh6eyFDC3ZhYmNLob18LjMgKmQFnIzX0ObS0F00ab8YhpdK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)