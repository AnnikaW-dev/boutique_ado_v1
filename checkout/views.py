from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in the bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RfhEjP00t3GaRQwFU23GC7jdwCvuMEQJSUMOYNrA1Ajt1bEyYSVWkvyU9EpZJVmrPjyTrgcBMJrrrb9eEuOxPxM00ue7OMGgy',
        'client-secret': 'test client secret',
    }

    return render(request, template, context)
