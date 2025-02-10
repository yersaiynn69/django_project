import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myProject.settings')

# Create the ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle HTTP requests with Django's ASGI application
    # Uncomment and configure WebSocket routing if using Channels for WebSockets
    # "websocket": AuthMiddlewareStack(URLRouter(your_websocket_routing_urlpatterns)),
})
