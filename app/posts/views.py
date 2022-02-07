from django.shortcuts import render

# dependencias para possibilitar a utilização das Class Based Views
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# importando a model Post
from .models import Post


class PostIndex(ListView):

    # atribuindo a model a ser utilizada
    model = Post

    # atribuindo o template a ser utilizado
    template_name = 'posts/index.html'

    context_object_name = 'posts'



class PostSearch(PostIndex):
    pass


class PostCategory(PostIndex):
    pass


class PostDetails(UpdateView):
    pass
