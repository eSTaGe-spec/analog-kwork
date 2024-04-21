from django.db import models
from django.contrib.auth.models import User


def upload_avatar(instance, filename):
    return 'profile/user_{pk}/avatar/{filename}'.format(
        pk=instance.user.pk,
        filename=filename
    )


class Executor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин пользователя')
    name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    about_me = models.TextField(verbose_name='Информация о пользователе')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    status = models.CharField(max_length=20, default='executor', verbose_name='Статус пользователя')
    avatar = models.ImageField(upload_to=upload_avatar, default=True, null=True, verbose_name='Аватар пользователя')

    def __str__(self):
        return self.user.username

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
    avatar = models.ImageField(upload_to=upload_avatar, verbose_name='Аватар пользователя', default=True, null=True)


    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'customer'
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

