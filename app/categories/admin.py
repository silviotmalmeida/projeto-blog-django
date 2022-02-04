from django.contrib import admin

from .models import Category # importando as models do app


# definindo as configurações de exibição da Category na área administrativa
class CategoryAdmin(admin.ModelAdmin):

    # definindo as colunas a serem exibidas
    list_display = ('id', 'name')

    # definindo em quais colunas serão colocados links de edição
    list_display_links = ('id', 'name')


# registrando as models para exibição na área administrativa
admin.site.register(Category, CategoryAdmin)
