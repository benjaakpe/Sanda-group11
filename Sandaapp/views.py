import email
from itertools import product

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from Sanda import settings
from .forms import UserRegisterForm, CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Sandaapp/home.html', context)


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        profile_form = CustomerForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            customer_profile = profile_form.save(commit=False)
            customer_profile.user = user
            customer_profile.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('Sandaapp:home')
    else:
        form = UserRegisterForm()
        profile_form = CustomerForm()

    return render(request, 'Sandaapp/signup.html', {'form': form, 'profile_form': profile_form})


def login(request):
    return render(request, 'Sandaapp/login.html', {'Sandaapp': login})


def cart(request):
    return render(request, 'Sandaapp/cart.html', {'Sandaapp': cart})


def checkout(request):
    """
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
        """
    context = {}

    return render(request, 'Sandaapp/checkout.html', context)


def logout(request):
    return render(request, 'Sandaapp/logout.html', {'Sandaapp': logout})


def password_reset(request):
    return render(request, 'Sandaapp/password_reset_form.html', {'Sandaapp': password_reset})


def password_reset_done(request):
    return render(request, 'Sandaapp/password_reset_done.html', {'Sandaapp': password_reset_done})


def send_email(request):
    subject = 'Sanda email confirmation'
    message = 'Please confirm your email below'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['minhvuvlbay@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    print('send_email')
    return HttpResponse(status=204)


@login_required
def customer_details(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'Sandaapp/customer_details.html', {'customers': customer})


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'Sandaapp/customer_list.html',
                          {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'Sandaapp/customer_edit.html', {'form': form})


def cart(request):
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    """
    context = {}

    return render(request, 'Sandaapp/cart.html', context)


def payment(request):
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    """
    context = {}

    return render(request, 'Sandaapp/payment.html', context)


def success(request):
    context = {}
    return render(request, 'Sandaapp/success.html', context)
