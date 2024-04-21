from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .models import Customer, Executor


def login(request):
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        role = request.POST.get('status')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        if role == 'executor':
            executor = Executor.objects.create(user=user)
            executor.save()
        elif role == 'customer':
            customer = Customer.objects.create(user=username, password=password)
            customer.save()

        authenticate(request, username=username, password=password)
        login(request)

        return redirect(reverse('main:profile'))

    return render(request, 'main/register.html')


def profile(request):
    return render(request, 'main/profile.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('main:login'))
