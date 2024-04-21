from django.urls import path
from django.contrib.auth.views import LoginView

from .views import register, profile, user_logout

app_name = 'main'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='main/login.html',
                                     redirect_authenticated_user=True), name='login'),

    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout')
]
