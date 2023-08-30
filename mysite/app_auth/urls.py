from django.urls import path
from .views import my_login, my_logout, my_profile, my_register

urlpatterns = [
    path('myauth/', my_login, name="login"),
    path('mylogout/', my_logout, name="logout"),
    path('myprofile/', my_profile, name='profile'),
    path('myregister', my_register, name='register')
]