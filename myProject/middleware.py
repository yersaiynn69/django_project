import os
from django.conf import settings
from django.http import HttpResponseForbidden
from geoip2.database import Reader
from geoip2.errors import AddressNotFoundError


class KazakhstanOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Путь к базе GeoIP
        db_path = os.path.join(settings.GEOIP_PATH, "GeoLite2-Country.mmdb")
        self.reader = Reader(db_path)

    def __call__(self, request):
        ip = self.get_client_ip(request)

        # Разрешаем localhost
        if ip in ("127.0.0.1", "localhost"):
            return self.get_response(request)

        try:
            response = self.reader.country(ip)
            country_code = response.country.iso_code

            # Разрешаем только Казахстан
            if country_code != "KZ":
                return HttpResponseForbidden("⛔ Access denied outside Kazakhstan.")
        except AddressNotFoundError:
            return HttpResponseForbidden("❗ IP address not found in GeoIP database.")
        except Exception:
            return HttpResponseForbidden("❌ GeoIP lookup failed.")

        return self.get_response(request)

    def get_client_ip(self, request):
        """Получает IP-адрес клиента из заголовков запроса."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            # Берёт первый IP (в случае, если их несколько)
            return x_forwarded_for.split(",")[0].strip()
        return request.META.get("REMOTE_ADDR")
