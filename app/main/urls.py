from django.urls import path
from django.contrib.auth.views import LoginView

from .views import register, user_profile, user_logout, main_page, UpdateProfile

app_name = 'main'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', LoginView.as_view(template_name='main/login.html',
                                     redirect_authenticated_user=True), name='login'),

    path('register/', register, name='register'),
    path('profile/<str:username>/', user_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('profile/update/<int:pk>', UpdateProfile.as_view(), name='profile_update')

]
