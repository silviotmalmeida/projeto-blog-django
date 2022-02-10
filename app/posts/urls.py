# importando as dependências padrão
from django.urls import path
from . import views

urlpatterns = [
    # definindo a url da página index
    path('', views.PostIndex.as_view(), name='index'),
    # definindo a url da página de posts por categoria
    path('category/<str:category>',
         views.PostCategory.as_view(), name='post_category'),
    # definindo a url da página de busca de posts
    path('busca/', views.PostSearch.as_view(), name='post_search'),
    # definindo a url da página de detalhes do post
    path('post/<int:pk>', views.PostDetails.as_view(), name='post_details'),

    # definindo a url para carregamento de dados de teste
    path('loadtestdata', views.loadtestdata, name='loadtestdata'),
]
