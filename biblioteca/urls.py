from django.urls import path
from biblioteca.views import index, artigo, buscar

urlpatterns = [
    path('', index),
    path('artigo', artigo),
    path('buscar', buscar, name='buscar')
]