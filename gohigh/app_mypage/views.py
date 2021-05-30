from django.shortcuts import render, redirect
from .models import Mypage
from app_registration.models import Profile
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def mypage(request):
    mypages = Profile.objects.filter(username=request.user)
    
    return render(request, 'mypage.html', {'mypages': mypages})

