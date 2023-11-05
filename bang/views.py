from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import *
from .models import Product, AboutMe

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
    return render(request, 'test/product.html', context=context)




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


class RegisterUser(FormView):
    form_class = RegisterUserForm
    template_name = 'test/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('/')




class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'test/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
