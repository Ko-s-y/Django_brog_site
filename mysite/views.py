from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Django Brog Site',
        'articles': articles,
	}
    return render(request, 'mysite/index.html', context)

def login(request):
    context = {}
    return render(request, 'mysite/login.html', context)
