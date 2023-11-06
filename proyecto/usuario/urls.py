from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm

app_name = 'usuario'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
