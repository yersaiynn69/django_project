import os
from django.conf import settings
from geoip2.database import Reader
from django.http import HttpResponseForbidden

class KazakhstanOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        db_path = os.path.join(settings.GEOIP_PATH, "GeoLite2-Country.mmdb")
        self.reader = Reader(db_path)

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        if ip == "127.0.0.1":  # allow local
            return self.get_response(request)

        try:
            response = self.reader.country(ip)
            if response.country.iso_code != "KZ":
                return HttpResponseForbidden("Access denied outside Kazakhstan.")
        except Exception:
            return HttpResponseForbidden("GeoIP lookup failed.")

        return self.get_response(request)
