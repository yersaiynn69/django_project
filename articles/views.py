from django.shortcuts import render, get_object_or_404

from articles.models import Articles


def service(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
        'title': 'Service',
    }
    return render(request, 'test/service.html', context=context)

def show_article(request, article_slug):
    article = get_object_or_404(Articles, slug=article_slug)

    context = {
        'article': article,
        'title': article.title,
    }
    return render(request, 'test/articles.html', context=context)



