from django.contrib.auth.decorators import login_required
import logging
from .decorators import base_view
from .forms import *
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

logger = logging.getLogger(__name__)

# Navigation bar content
menu = [
    {'title': "Catalog", 'url_name': 'catalog'},
    {'title': "Service", 'url_name': 'appointments'},
    {'title': "Product", 'url_name': 'product'},
    {'title': "Contact", 'url_name': 'contact'},
]


# Function to return main page
def index(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'test/index.html', context=context)


# Function to return home page
def home(request):
    return render(request, 'test/index.html', {'title': 'Bang.in'})

def householdDoctor(request):
    return render(request, 'test/householdDoctor.html', {'title': 'householdDoctor'})

# Function to return Service page

# Function to return Product page
def product(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Catalog',
    }
    return render(request, 'test/catalog.html', context=context)


# Function to show the post
@login_required()
def show_post(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    if request.method == "POST":
        form = PayForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            print(form.cleaned_data)
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error, f'Something is wrong!')
    else:
        form = PayForm()

    context = {
        'form': form,
        'post': post,
        'menu': menu,
        'title': post.title,
    }
    return render(request, 'test/product.html', context=context)


# Function to return settings page
@login_required()
def setting(request):
    return render(request, 'test/setting.html', {'title': 'Settings'})


# Feedback function
@base_view
@login_required()
def contact_formview(request):
    try:
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.save()
                print(form.cleaned_data)
                return redirect('home')

            else:
                for error in list(form.errors.values()):
                    messages.error(request, error, f'Something is wrong!')
                    logger.exception('Something is wrong!')

        else:
            form = FeedbackForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {e}", 'Something is wrong!')
        logger.exception('Something is wrong!')
    return render(
        request=request,
        template_name='test/contact.html',
        context={"form": form}
    )



