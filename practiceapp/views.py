from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm, UserProfileForm
from .filters import OrderFilter
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated
from django.contrib.auth.models import Group
from .decorators import admin_only


# Create your views here.
def user_settings(request):
    customer = request.user.customer
    form = UserProfileForm(instance=customer)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'practiceapp/user_settings.html', context)


def user_page(request):
    customer_orders = request.user.customer.order_set.all()
    total_orders = customer_orders.count()
    delivered = customer_orders.filter(status='Delivered').count()
    pending = customer_orders.filter(status='Pending').count()

    context = {
        'customer_orders': customer_orders,
        'delivered': delivered, 'pending': pending,
        'total_orders': total_orders,
    }
    return render(request, 'practiceapp/userPage.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Incorrect Uername or Password')
    context = {

    }
    return render(request, 'practiceapp/login.html', context)


@unauthenticated
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, 'Account registered for %s', username)
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'practiceapp/registration.html', context)


@admin_only
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


@login_required(login_url='login')
def product(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'practiceapp/product.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    formset = OrderFormSet(queryset=Customer.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset': formset
    }
    return render(request, 'practiceapp/createOrder.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'formset': form
    }
    return render(request, 'practiceapp/createOrder.html', context)


@login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'practiceapp/deleteOrder.html', context)


@login_required(login_url='login')
def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'practiceapp/createCustomer.html', context)


@login_required(login_url='login')
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return      redirect('/')
    context = {
        'form': form
    }
    return render(request, 'practiceapp/createCustomer.html', context)