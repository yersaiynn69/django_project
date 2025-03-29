from django.http import HttpResponseForbidden
from geoip2.database import Reader
import logging

logger = logging.getLogger(__name__)

class KazakhstanOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.geo = GeoIP2()

    def __call__(self, request):
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0]

        try:
            country = self.geo.country(ip)['country_name']
        except Exception as e:
            logger.warning(f"🌍 Не удалось определить страну для IP {ip}: {e}")
            return HttpResponseForbidden("⛔ Доступ разрешён только из Казахстана")

        if country != 'Kazakhstan':
            logger.warning(f"🚫 Блок: IP {ip}, страна: {country}")
            return HttpResponseForbidden("⛔ Доступ только из Казахстана")

        return self.get_response(request)
