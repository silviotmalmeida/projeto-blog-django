from django.contrib import admin
# importando as models do app
from .models import Categoria


# definindo as configurações de exibição da Categoria na área administrativa
class CategoriaAdmin(admin.ModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'nome')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('id', 'nome')


# registrando as models para exibição na área administrativa
admin.site.register(Categoria, CategoriaAdmin)
