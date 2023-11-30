from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'blog/article.html', context)
