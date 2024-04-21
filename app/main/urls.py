from django.urls import path

from .views import login, register, profile

app_name = 'main'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
