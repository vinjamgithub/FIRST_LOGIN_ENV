from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


#router = routers.DefaultRouter()
#router.register('credentials', views.credentialsViewSet )

urlpatterns = [

    path('', views.home, name="home"),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('studentmarks',views.studentmarks, name='studentmarks'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]


