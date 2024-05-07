from about_us.models import AboutUs
from django.shortcuts import render

# Function to return Info About us page
def about_us(request):
    posts = AboutUs.objects.all()
    odd_posts = posts[0::2]
    even_posts = posts[1::2]
    context = {
        'posts': posts,
        'title': 'About Us',
        'odd_posts': odd_posts,
        'even_posts': even_posts,
    }
    return render(request, 'test/about_us.html', context=context)