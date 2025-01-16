from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_request, name='logout'),
    path('Books/', views.Books, name='Books'),
    path('members/', views.members, name='members'),
    path('member/<int:pk>/', views.member, name='member'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_member/', views.add_member, name='add_member'),
    path('edit/<int:pk>/', views.edit , name='edit'),
    path('aboutbook/<int:pk>/', views.aboutbook, name='aboutbook'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),
    path('return_book/<int:pk>/', views.return_book, name='return_book'),
    path('add_borrow/', views.add_borrow, name='add_borrow'),
]

