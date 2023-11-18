from django.contrib import admin
from biblioteca.models import Artigo
# Register your models here.

class ListArtigos(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'data_publicacao','publicado')
    list_filter = ('autor', 'titulo', 'publicado','data_publicacao')
    search_fields = ('autor', 'titulo', 'publicado','data_publicacao')
    list_display_links = ('autor', 'titulo')
    list_editable = ('publicado',)


admin.site.register(Artigo, ListArtigos)