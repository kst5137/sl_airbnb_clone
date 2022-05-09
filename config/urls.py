"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

import airbnb.views
import board
from board import views

urlpatterns = [
    path('airbnb/', airbnb.views.index, name='index'),
    path('airbnb/host/main', airbnb.views.hostpage_main, name='host_main'),
    path('airbnb/login', airbnb.views.login, name='login'),
    path('airbnb/host/register', airbnb.views.register, name='register'),
    path('airbnb/room', airbnb.views.room, name='room'),
    path('airbnb/room2', airbnb.views.room, name='room2'),

    path('boardRegister/', board.views.register),

]
