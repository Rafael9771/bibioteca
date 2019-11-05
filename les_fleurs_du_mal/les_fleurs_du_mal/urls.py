
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views



urlpatterns = [

   
    path('', include('aplications.biblioteca.urls')),


]
