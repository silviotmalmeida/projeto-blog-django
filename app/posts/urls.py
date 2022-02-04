# importando as dependências padrão
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),  # definindo a url da página index
    # definindo a url da página de posts por categoria
    path('category/<str:category>', views.PostCategory.as_view(), name='post_category'),
    # definindo a url da página de busca de posts
    path('busca/', views.PostSearch.as_view(), name='post_search'),
    # definindo a url da página de detalhes do post
    path('post/<int:id>', views.PostDetails.as_view(), name='post_details'),
]
