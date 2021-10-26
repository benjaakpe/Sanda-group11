from django.shortcuts import redirect, render


def home(request):
    return render(request, 'Sandaapp/home.html', {'Sandaapp': home})
