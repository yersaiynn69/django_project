from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bang.urls')),
    path('', include('articles.urls')),
    path('', include('chat.urls')),
    path('', include('authentication.urls')),
    path('',include('about_us.urls')),
    path('captcha/', include('captcha.urls')),
    re_path('', include('social_django.urls', namespace='social')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
