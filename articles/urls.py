from django.urls import path

from articles.views import *

urlpatterns = [
    path('service/', service, name='service'),
    path('post/<slug:post_slug>/,', show_post, name='post'),
]
