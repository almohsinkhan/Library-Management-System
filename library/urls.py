from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_request, name='logout'),
    path('Books/', views.Books, name='Books'),
    path('members/', views.members, name='members'),
    path('member/<int:pk>/', views.member, name='member'),
]