from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,  login
from django.contrib.auth.decorators import login_required
from authentication.models import credentials
from . models import credentials
from rest_framework import generics
from .serializers import credentialsSerializer
from rest_framework import viewsets

# Create your views here.
def home(request):
    cred = credentials.objects.all()
    
    return render(request, "index.html",{'cred':cred})

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        #pass2 = request.POST['pass2']

        myuser = credentials(username=username,fname=fname, lname=lname, email=email,pass1=pass1 )
        myuser.save()
        messages.success(request,'your account has been succesfully created.')
        return redirect('home')    
    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        #user = authenticate(username=username,pass1=pass1)
        if username == username and pass1 == pass1:    
            print('user sucessfully login')
            return render(request, "studentmarks.html")
        else :
            return messages ('wrong credentials ')
        
    return render(request, "signin.html")
def studentmarks(request):
    return render(request, "studentmarks.html")

