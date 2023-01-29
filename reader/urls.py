from django.urls import path 
from . import views 

urlpatterns = [
    path('view/', views.view), 
    path('main/', views.main),
    path('main/table.html', views.table),
    path('main/main.html', views.main),
    path('main/login.html', views.login),
    path('main/sign up.html', views.register),   
    path('main/schedule.html', views.upload)
]