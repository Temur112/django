from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='users'
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('createprofile/', views.create_profile, name='create_profile'),
    path('sellerprofile/<int:id>', views.seller_profile, name='seller_profile'),
]
