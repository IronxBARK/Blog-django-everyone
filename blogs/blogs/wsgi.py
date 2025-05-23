"""
WSGI config for blogs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogs.settings')

application = get_wsgi_application()

# Ensure the WSGI application is ready for production
# Use a WSGI server like Gunicorn or uWSGI to serve this application in production
