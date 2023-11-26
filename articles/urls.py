from django.urls import path

from articles.views import *

urlpatterns = [
    path('service/',  ServiceView.as_view(), name='service'),
    path('service/<slug:article_slug>/,',  ArticleDetailView.as_view(), name='show_article'),
]
