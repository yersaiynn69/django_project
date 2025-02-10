from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='home'),
    path('product/', product, name='product'),
    path('contact/', contact_formview, name='contact'),
    path('setting', setting, name='setting'),
    path('householdDoctor', householdDoctor, name='householdDoctor'),

    path('post/<slug:post_slug>/,', show_post, name='post'),
]
