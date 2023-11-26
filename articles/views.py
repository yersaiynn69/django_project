from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse

from articles.models import Articles

class ServiceView(View):
    template_name = 'service.html'

    def get(self, request, *args, **kwargs):
        # Get all articles from the database
        articles = Articles.objects.all()

        # Creating a context to pass to the template
        context = {
            'articles': articles,
            'title': 'Service',
        }

        # Return an HTTP response with the rendered template and context
        return render(request, self.template_name, context=context)

class ArticleDetailView(View):
    template_name = 'articles.html'

    def get(self, request, article_slug, *args, **kwargs):
        # Get an article by its unique identifier (slug)
        article = get_object_or_404(Articles, slug=article_slug)

        # Creating a context to pass to the template
        context = {
            'article': article,
            'title': article.title,
        }

        # Return an HTTP response with the rendered template and context
        return render(request, self.template_name, context=context)
