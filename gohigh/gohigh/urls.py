"""gohigh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.presetting, name='presetting')
Class-based views
    1. Add an import:  from other_app.views import presetting
    2. Add a URL to urlpatterns:  path('', presetting.as_view(), name='presetting')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_registration.views import start, temp_home, presetting, signup, login, login2, logout, activate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start, name='start'),
    path('temp_home/', temp_home, name="temp_home"),
    path('presetting/', presetting, name="presetting"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('login2/<int:Profile_pk>', login2, name="login2"),
    path('logout/', logout, name="logout"),
    path('activate/<str:uidb64>/<str:token>/', activate, name="activate"),
    path('study/', include('app_study.urls')),
]