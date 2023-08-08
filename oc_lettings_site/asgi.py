"""
OC Lettings Site - ASGI Configuration

This module contains the ASGI configuration for the OC Lettings Site.

Attributes:
    application: The ASGI application instance for the OC Lettings Site.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
