"""project URL Configuration

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
from django.urls import path, include
from app import views

urlpatterns = [
    path('registration/signup', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('registration/logout', views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('mypage', views.mypage, name='mypage'),
    path('home/detail/<int:final_select_num>/', views.detail, name='detail'),
]
