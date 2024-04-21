from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.forms import forms
from django.forms.models import model_to_dict, modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from .models import Customer, Executor


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
            customer = Customer.objects.create(user=user)
            customer.save()

        login(request, user)

        return redirect(reverse('main:main_page'))

    return render(request, 'main/register.html')


def user_profile(request, username):
    if Executor.objects.filter(user=request.user).exists():
        profile = Executor.objects.get(user=request.user)
        status = 'Исполнитель'
    elif Customer.objects.filter(user=request.user).exists():
        profile = Customer.objects.get(user=request.user)
        status = 'Заказчик'

    context = {
        'profile': profile,
        'status': status,
    }

    return render(request, 'main/profile.html', context)


def user_logout(request):
    logout(request)
    return redirect(reverse('main:login'))


def main_page(request):
    customer = Customer.objects.all()
    executor = Executor.objects.all()

    context = {
        'customers': customer,
        'customer_status': 'Заказчик',
        'executors': executor,
        'executor_status': 'Исполнитель',
    }

    return render(request, 'main/main_page.html', context)


class UpdateProfile(UpdateView):
    fields = ['name', 'about_me', 'work_experience', 'phone', 'email', 'avatar']
    template_name = 'main/profile_update.html'

    def get_object(self, queryset=None):
        if Executor.objects.filter(user=self.request.user).exists():
            return Executor.objects.get(user=self.request.user)
        elif Customer.objects.filter(user=self.request.user).exists():
            return Customer.objects.get(user=self.request.user)
        return None

    def get_success_url(self):
        return reverse(
            'main:profile',
            kwargs={'username': self.object.user.username}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context

