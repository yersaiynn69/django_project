import functools
import traceback

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View


def user_not_authenticated(function=None, redirect_url='/'):
    """
    Decorator for views that checks that the
    user is NOT logged in, redirecting
    to the homepage if necessary by default.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator


JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}
def ret(json_object, status=200):
    return JsonResponse(
        json_object,
        status=status,
        safe = not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )

def error_response(exception):
    """
    Formats HTTP response with
    error description and Traceback
    """
    res = {
        "errorMessage": str(exception),
        "traceback": traceback.format_exc()
    }
    return ret(res, status=400)


def base_view(fn):
    """
    Decarator for all views
    that handles exceptions
    """

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)

    return inner




class BaseView(View):
    """
    Class-based decorator for all views
    that handles exceptions
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return self._response({'errorMessage': e.message}, status=400)

        if isinstance(response, (dict,list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS
        )





