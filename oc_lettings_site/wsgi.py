"""
OC Lettings Site - WSGI Configuration

This module contains the WSGI configuration for the OC Lettings Site.

Attributes:
    application: The WSGI application instance for the OC Lettings Site.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
