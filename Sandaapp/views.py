import email

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from Sanda import settings
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Customer


def home(request):
    return render(request, 'Sandaapp/home.html', {'Sandaapp': home})


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('Sandaapp:home')
    else:
        form = UserRegisterForm()

    return render(request, 'Sandaapp/signup.html', {'form': form})


def login(request):
    return render(request, 'Sandaapp/login.html', {'Sandaapp': login})


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


def customer_details(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'Sandaapp/customer_details.html', {'customers': customer})

