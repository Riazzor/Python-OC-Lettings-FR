"""
OC Lettings Site - Admin Registration for Profile Model

This module registers the 'Profile' model with the Django admin site.

Registered Model:
    Profile: The 'Profile' model from the 'profiles' app.
"""
from django.contrib import admin
from profiles.models import Profile


admin.site.register(Profile)
