from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article
    }

    return render(request, 'blog/article.html', context)
