from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .decorators import user_not_authenticated
from .forms import *
from .models import Product, AboutMe
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token

menu = [{'title': "Catalog", 'url_name': 'catalog'},
        {'title': "Service", 'url_name': 'service'},
        {'title': "Product", 'url_name': 'product'},
        {'title': "Contact", 'url_name': 'contact'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context


def index(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }

    return render(request, 'test/index.html', context=context)





def home(request):
    return render(request, 'test/index.html', {'title': 'Bang.in'})


def service(request):
    return render(request, 'test/service.html', {'title': 'Service'})


def product(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Catalog',
    }
    return render(request, 'test/catalog.html', context=context)


def about_us(request):
    posts = AboutMe.objects.all()
    odd_posts = posts[0::2]
    even_posts = posts[1::2]
    context = {
        'posts': posts,
        'title': 'About Us',
        'odd_posts': odd_posts,
        'even_posts': even_posts,
    }
    return render(request, 'test/about_us.html', context=context)


@login_required()
def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'test/post.html', context=context)


def setting(request):
    return render(request, 'test/setting.html', {'title': 'Settings'})


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'test/login.html'


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('homepage')


def activateEmail(request, user, to_email):
    # mail_subject = "Activate your user account."
    # message = render_to_string("test/template_activate_account.html", {
    #     'user': user.username,
    #     'domain': get_current_site(request).domain,
    #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #     'token': account_activation_token.make_token(user),
    #     "protocol": 'https' if request.is_secure() else 'http'
    # })
    # email = EmailMessage(mail_subject, message, to=[to_email])
    # if email.send():
    messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')


# else:
#     messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error, f'LOOOOOOOOOOOOOL')

    else:
        form = RegisterUserForm()

    return render(
        request=request,
        template_name="test/registration.html",
        context={"form": form}
    )


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required()
def contactFormView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            print(form.cleaned_data)
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error, f'Something is wrong!')

    else:
        form = ContactForm()

    return render(
        request=request,
        template_name='test/contact.html',
        context={"form": form}
    )
