"""
OC Lettings Site - Admin Registration for Letting and Address Models

This module registers the 'Letting' and 'Address' models with the Django admin site.

Registered Models:
    Letting: The 'Letting' model from the 'lettings' app.
    Address: The 'Address' model from the 'lettings' app.
"""
from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address


admin.site.register(Letting)
admin.site.register(Address)
