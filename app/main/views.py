from django.shortcuts import render


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')


def profile(request):
    return render(request, 'main/profile.html')
