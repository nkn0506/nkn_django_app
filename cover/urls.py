from typing import ValuesView
from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.views.generic.base import TemplateView
from cover import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='index'),
    path("base/",views.base, name='base'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("works/", views.works, name='works'),
    path("login/", auth_views.LoginView.as_view(template_name='cover/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='cover/logout.html '), name='logout'),
    path("register/",views.registerpage, name='register'),
    
]
