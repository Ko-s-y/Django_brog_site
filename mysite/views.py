from django.shortcuts import render
from django.contrib.auth.views import LoginView
from blog.models import Article

def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Django Brog Site',
        'articles': articles,
	}
    return render(request, 'mysite/index.html', context)

class Login(LoginView):
    template_name = 'mysite/login.html'
