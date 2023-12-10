from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Article, Comment

def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    context = {
        'pagi_articles': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article)
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'blog/article.html', context)
