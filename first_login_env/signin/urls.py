
from django.urls import path , include
from django.contrib import admin
from . import views
from .views import RegisterAPI

urlpatterns = [
    
    #path('', views.registration, name="registration"),
    #path('regsignup', views.regsignup, name="regsignup"),
    #path('Login',views.Login, name = 'Login')
    
    path('api/register/', RegisterAPI.as_view(), name='register'),
]
