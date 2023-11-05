from django.shortcuts import render, get_object_or_404

from articles.models import Articles


def service(request):
    posts = Articles.objects.all()
    context = {
        'posts': posts,
        'title': 'Service',
    }
    return render(request, 'test/service.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Articles, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'test/post.html', context=context)



