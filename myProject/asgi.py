import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')

# Create the ASGI application
application = get_asgi_application()
