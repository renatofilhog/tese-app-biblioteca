from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField()
    autor = models.CharField(max_length=100)
    palavras_chave = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='artigos/', null=True, blank=True)
    publicado = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    data_publicacao = models.DateField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.autor} - {self.titulo} - {self.data_publicacao}"