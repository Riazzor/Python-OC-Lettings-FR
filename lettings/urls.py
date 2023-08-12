"""
Lettings App - URL Configuration

This module contains the URL configuration for the 'lettings' app.

URL Patterns:
    '' (index): URL pattern for the index view.
    '<int:letting_id>/' (letting): Dynamic URL pattern for individual lettings.

Attributes:
    app_name (str): The namespace for the 'lettings' app.
"""
from django.urls import path
from lettings import views


app_name = 'lettings'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
