from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Django Brog Site'
	}
    return render(request, 'mysite/index.html', context)
