from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='home'),
    path('product/', product, name='product'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about_us/', about_us, name='about_us'),
    path('login/', LoginUser.as_view(), name='login'),
    path('setting', setting, name='setting'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path('post/<slug:post_slug>/,', show_post, name='product'),



]
