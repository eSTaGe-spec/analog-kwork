from django.urls import path

from .views import login, register

app_name = 'main'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
