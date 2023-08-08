"""
OC Lettings Site - URL Configuration

This module contains the URL configuration for the OC Lettings Site.

URL Patterns:
    '' (index): The root URL, mapped to the index view.
    'lettings/' (lettings): Includes URL patterns from the 'lettings' app.
    'profiles/' (profiles): Includes URL patterns from the 'profiles' app.
    'admin/' (admin): The Django admin panel URL.

Note:
    This configuration uses the 'include' function to include URL patterns from other apps.
"""
from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
