from django.db import models
from django.contrib.auth.models import User


class Executor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин пользователя')
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    about_me = models.TextField(verbose_name='Информация о пользователе')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    status = models.CharField(max_length=20, default='executor', verbose_name='Статус пользователя')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'executor'
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин пользователя')
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    about_me = models.TextField(verbose_name='Информация о пользователе')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    status = models.CharField(max_length=20, default='customer', verbose_name='Статус пользователя')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

