from django.contrib import admin
# importando as models do app
from .models import Post
# importando o editor de texto summernote
from django_summernote.admin import SummernoteModelAdmin


# definindo as configurações de exibição do Post na área administrativa
# herdando as funções do summernote
class PostAdmin(SummernoteModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'titulo', 'id_autor', 'data', 'id_categoria', 'publicado')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('id', 'titulo')

    # definindo as colunas liberadas para ediçao na tela de listagem
    list_editable = ('publicado',)

    # definindo os caompos para integração com o summernote
    summernote_fields = ('conteudo',)


# registrando as models para exibição na área administrativa
admin.site.register(Post, PostAdmin)
