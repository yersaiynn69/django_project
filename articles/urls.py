from django.urls import path

from articles.views import *

urlpatterns = [
    path('service/', service, name='service'),
    path('service/<slug:article_slug>/,', show_article, name='show_article'),
]
