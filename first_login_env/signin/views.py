
from typing import Self
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import userlogin
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import  auth
from signin.models import userlogin 
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework import status
from .serializers import userloginSerializer
from rest_framework import generics, permissions
from knox.models import AuthToken
from rest_framework.response import Response
#from .serializers import userloginSerializer, RegisterSerializer

class RegisterAPI(generics.GenericAPIView):
    #serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": userloginSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

