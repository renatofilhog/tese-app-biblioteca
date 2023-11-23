from django.http import HttpResponse
from django.shortcuts import render
from biblioteca.models import Artigo
# Create your views here.

def index(request):
    lst = Artigo.objects.all()
    return render(request, 'biblioteca/index.html',  {'artigos': lst})

def artigo(request):
    return render(request, 'biblioteca/artigo.html')

def buscar(request):
    artigos = Artigo.objects.order_by("data_publicacao").filter(publicado=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            artigos = artigos.filter(titulo__icontains=nome_a_buscar)
    return render(request, 'biblioteca/buscar.html', {'artigos': artigos})
