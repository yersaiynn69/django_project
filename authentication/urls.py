from django.contrib.auth import views
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
]
