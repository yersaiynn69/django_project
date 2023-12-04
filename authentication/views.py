from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from bang.decorators import BaseView
from authentication.forms import *
from django.shortcuts import redirect
from django.contrib.auth import logout

from bang.utils import grecaptcha_verify


# Login

class LoginUser(LoginView, BaseView):
    template_name = 'login.html'
    form_class = LoginUserForm
    success_url = 'home'

    # Validation
    def form_valid(self, form):
        print("Start of LoginUser view")  # For debugging

        # Current logic

        # check reCAPTCHA
        recaptcha_response = grecaptcha_verify(self.request)
        print("recaptcha_response:", recaptcha_response)  # For debugging

        if recaptcha_response.get("status"):
            # Logic for success
            print('User logged successfully')
            return super().form_valid(form)
        else:
            # Logic for failed verification
            return self.form_invalid(form)

# Registration
class RegisterUser(FormView, BaseView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        print('User registered succesfully')
        return super().form_valid(form)

# Logout
def logout_user(request):
    logout(request)
    print('User logged out')
    return redirect('/')