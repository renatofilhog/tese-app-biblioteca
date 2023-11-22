from django.http import HttpResponse
from django.shortcuts import render
from biblioteca.models import Artigo
# Create your views here.

def index(request):
    lst = Artigo.objects.all()
    return render(request, 'biblioteca/index.html',  {'artigos': lst})

def artigo(request):
    return render(request, 'biblioteca/artigo.html')