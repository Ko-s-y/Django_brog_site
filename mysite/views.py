from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm
from blog.models import Article
from django.contrib import messages

def index(request):
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Django Brog Site',
        'articles': articles,
	}
    return render(request, 'mysite/index.html', context)

class Login(LoginView):
    template_name = 'mysite/auth.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログインが完了しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'ログインに失敗しました！')
        return super().form_invalid(form)

def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, '登録が完了しました！')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)

def mypage(request):
    context = {}
    return render(request, 'mysite/mypage.html', context)
