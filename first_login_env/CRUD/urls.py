from django.contrib import admin
from django.urls import path, include
from . import views
    
urlpatterns = [
    
   path('emplist/', views.emplist, name="emplist"),
   path('empform/', views.empform, name="empform"),
   path('<int:id>/', views.empform, name='empupdate'),
   path('delete/<int:id>/', views.empdelete, name = 'empdelete')
   ]