from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='home'),
    path('product/', product, name='product'),
    path('contact/', contactFormView, name='contact'),
    path('about_us/', about_us, name='about_us'),
    path('setting', setting, name='setting'),
    path('post/<slug:post_slug>/,', show_post, name='post'),
]
