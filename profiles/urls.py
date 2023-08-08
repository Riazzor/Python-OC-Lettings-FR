"""
Profiles App - URL Configuration

This module contains the URL configuration for the 'profiles' app.

URL Patterns:
    '' (index): The root URL, mapped to the index view for profile.
    '<str:username>/' (profile): Dynamic URL pattern for user profiles.

Attributes:
    app_name (str): The namespace for the 'profiles' app.
"""
from django.urls import path
from profiles import views


app_name = 'profiles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
