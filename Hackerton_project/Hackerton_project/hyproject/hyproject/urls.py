"""hyproject URL Configuration

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
from hyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('signup/', views.signup, name="signup"),
    path('main/', views.main, name="main"),
    path('login/', views.login, name="login"),
    path('mysubject/<int:user_pk>', views.mysubject, name="mysubject"),
    path('detail/<int:subject_pk>', views.detail, name="detail"),
    path('logout', views.logout, name="logout"),
    path('home', views.home, name="home"),
    path('home_select', views.home_select, name="home_select"),
    path('study/', views.study, name="study"),
    path('click_start/', views.click_start, name="click_start"),
    # path('recordlist/', views.recordlist, name="recordlist"),
    # path('checkcomplete/<int:pk>', views.checkcomplete, name ="checkcomplete"),
]
