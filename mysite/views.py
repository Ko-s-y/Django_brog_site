from django.shortcuts import render
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm
from blog.models import Article

def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Django Brog Site',
        'articles': articles,
	}
    return render(request, 'mysite/index.html', context)

class Login(LoginView):
    template_name = 'mysite/auth.html'

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # user.is_activa = False
            user.save()
            return redirect('/')
    return render(request, 'mysite/auth.html', context)
