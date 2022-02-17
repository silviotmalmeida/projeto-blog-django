from django.contrib import admin
# importando as models do app
from .models import Comentario


# definindo as configurações de exibição do Comentario na área administrativa
class ComentarioAdmin(admin.ModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'nome', 'email', 'data', 'id_post', 'publicado')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('id', 'nome')

    # definindo o limite de registros por página
    list_per_page = 10

    # definindo as colunas a serem consideradas no campo de pesquisa
    search_fields = ('nome', 'email',)

    # definindo as colunas liberadas para ediçao na tela de listagem
    list_editable = ('publicado',)


# registrando as models para exibição na área administrativa
admin.site.register(Comentario, ComentarioAdmin)
