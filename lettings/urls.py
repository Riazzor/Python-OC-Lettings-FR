"""
Lettings App - URL Configuration

This module contains the URL configuration for the 'lettings' app.

URL Patterns:
    'lettings/' (index): URL pattern for the index view.
    'lettings/<int:letting_id>/' (letting): Dynamic URL pattern for individual lettings.

Attributes:
    app_name (str): The namespace for the 'lettings' app.
"""
from django.urls import path
from lettings import views


app_name = 'lettings'
urlpatterns = [
    path('lettings/', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
