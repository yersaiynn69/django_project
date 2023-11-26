from django.urls import re_path

from chat import consumers


# Define WebSocket URL patterns for Django Channels
websocket_urlpatterns = [
    # Use re_path to define a URL pattern with a regular expression
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi())
]