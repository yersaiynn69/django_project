from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('home', index, name='home'),
    path('product/', product, name='product'),
    path('contact/', contactFormView, name='contact'),
    path('about_us/', about_us, name='about_us'),
    path('login/', LoginUser.as_view(), name='login'),
    path('setting', setting, name='setting'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path('post/<slug:post_slug>/,', show_post, name='post'),
    path('activate/<uidb64>/<token>', activate, name='activate')



]
