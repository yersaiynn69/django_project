from bang.views import index
from chat.views import room
from django.urls import path

urlpatterns = [
    path('chat/<str:room_name>/', room, name='room'),
]