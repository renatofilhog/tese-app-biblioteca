from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'biblioteca/index.html')

def artigo(request):
    return render(request, 'biblioteca/artigo.html')