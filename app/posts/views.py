from django.shortcuts import render

# dependencias para possibilitar a utilização das Class Based Views
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


class PostIndex(ListView):
    pass


class PostSearch(PostIndex):
    pass


class PostCategory(PostIndex):
    pass


class PostDetails(UpdateView):
    pass
