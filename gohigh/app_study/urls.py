from django.contrib import admin
from django.urls import path
from app_study import views

urlpatterns =[
    path('', views.studyhome, name ="studyhome"),
    path('new/', views.new, name= "new"),
    path('detail/<int:study_pk>', views.detail, name ="detail"),
    path('category/<str:category_name>', views.category, name="category"),
    path('join', views.join, name="join"),
  
]