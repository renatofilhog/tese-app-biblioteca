from django.urls import path
from biblioteca.views import index, artigo

urlpatterns = [
    path('', index),
    path('artigo', artigo),
]