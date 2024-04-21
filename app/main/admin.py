from django.contrib import admin

from .models import Executor, Customer


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'email']
    list_display_links = ['user']


@admin.register(Customer)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'email']
    list_display_links = ['user']

