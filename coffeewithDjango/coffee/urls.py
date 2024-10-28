"""
URL configuration for coffeewithDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include  #include is to include app urls
from . import views

# localhost:8000/coffee
# localhost:8000/coffee/order  
urlpatterns = [
    path('', views.all_coffee, name='all_coffee'),
    path('<int:coffee_id>', views.coffee_detail, name='coffee_detail'), #if there's any integer after coffee/ it will treat it as coffee_id

   
]
