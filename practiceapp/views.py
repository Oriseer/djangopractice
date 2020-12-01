from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.forms import inlineformset_factory

# Create your views here.

def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders, 'customers': customers,
        'delivered': delivered, 'pending': pending,
        'total_orders': total_orders,
    }
    return render(request, 'practiceapp/dashboard.html', context)


def product(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'practiceapp/product.html', context)


def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    customer_orders = customers.order_set.all()
    total_orders = customer_orders.count()

    order_filter = OrderFilter(request.GET, queryset=customer_orders)
    customer_orders = order_filter.qs
    context = {
        'customer_orders': customer_orders,
        'customers': customers,
        'total_orders': total_orders,
        'order_filter': order_filter
    }
    return render(request, 'practiceapp/customer.html', context)


def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    formset = OrderFormSet(queryset=Customer.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('')
    context = {
        'formset': formset
    }
    return render(request, 'practiceapp/createOrder.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'practiceapp/createOrder.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'practiceapp/deleteOrder.html', context)