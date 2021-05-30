"""Hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signup_done/', views.signup_done, name='signup_done'),
    path('email/opt', views.email_opt, name='email_opt'),
    path('chat/<str:lecture_pk>', views.chat, name="chat"),
    path('search/', views.SearchFormView.as_view(), name='search'),
    path('mypage/', views.mypage, name="mypage"),
    path('add_lecture/<str:lecture_pk>', views.add_lecture, name="add_lecture"),
    path('logout', views.logout, name="logout"),
]