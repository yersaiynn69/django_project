# utils.py
import requests
from django.conf import settings
from ipware import get_client_ip

# Check Google reCaptcha
def grecaptcha_verify(request):
    response = {}
    data = request.POST
    captcha_rs = data.get('g-recaptcha-response')
    url = "https://www.google.com/recaptcha/api/siteverify"
    params = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': captcha_rs,
        'remoteip': get_client_ip(request)
    }

    try:
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs.raise_for_status()  # Checking for errors in the request

        verify_rs = verify_rs.json()
        response["status"] = verify_rs.get("success", True)
        response['message'] = verify_rs.get('error-codes', None) or "Success."

    except requests.RequestException as e:
        response["status"] = False
        response["message"] = f"Request error: {e}"

    return response
