"""
URL configuration for sls project.

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
from django.urls import path
from . import views


urlpatterns = [

    path('', views.HomePage, name='home'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),


    path('dashboard/', views.index, name='index'),
    path('all_event', views.all_event, name='all_event'),
    path('add_event', views.add_event, name='add_event'),
    path('remove_event', views.remove_event, name='remove_event'),
    path('remove_event/<int:org_id>', views.remove_event, name='remove_event'),
    path('filter_event', views.filter_event, name='filter_event'),

]
