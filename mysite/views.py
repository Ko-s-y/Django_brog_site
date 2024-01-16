from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm, ProfileForm
from blog.models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    ranks = Article.objects.order_by('-count')[:2]
    articles = Article.objects.all()[:3]
    context = {
        'title': 'Django Brog Site',
        'articles': articles,
        'ranks': ranks,
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
            login(request, user) # 登録後にログインさせる
            messages.success(request, '登録が完了しました！')
            return redirect('/')
    return render(request, 'mysite/auth.html', context)

@login_required
def mypage(request):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '登録完了しました')
    return render(request, 'mysite/mypage.html', context)

def contact(request):
    context = {}

    from django.core.mail import send_mail
    import os
    subject = '題名'
    message = '本文'
    email_from = os.environ['DEFAULT_EMAIL_FROM']
    email_to = [
        os.environ['DEFAULT_EMAIL_FROM'],
    ]
    send_mail(subject, message, email_from, email_to)

    return render(request, 'mysite/contact.html', context)
