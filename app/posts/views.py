from django.shortcuts import render, redirect

# dependencias para possibilitar a utilização das Class Based Views
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# importando a model Post
from .models import Post

from categories.models import Categoria
from comments.models import Comentario

# importando a model User da área administrativa do django
from django.contrib.auth.models import User

# dependências para querys complexas
from django.db.models import Q, Count, Case, When

# biblioteca de números aleatórios
import random


class PostIndex(ListView):

    # atribuindo a model a ser utilizada
    model = Post

    # atribuindo o template a ser utilizado
    template_name = 'posts/index.html'

    # definindo a quantidade de itens por página
    paginate_by = 6

    # determinando o nome do objeto a ser passado ao template
    context_object_name = 'posts'

    # sobreescrevendo a query padrão do django
    def get_queryset(self):

        # chamando o método da superclasse
        qs = super().get_queryset()

        # qs = qs.select_related('categoria_post')

        # filtrando por publicado=True e ordenando de forma decrescente por id
        qs = qs.order_by('-id').filter(publicado=True)

        # criando um campo anotado para calcular os comentários publicados do post
        qs = qs.annotate(

            # calculando os comentários que o atributo publicado=True
            comentarios_publicados=Count(
                Case(
                    When(comentario__publicado=True, then=1)
                )
            )
        )

        # retornando a query
        return qs


class PostSearch(PostIndex):

    # atribuindo o template a ser utilizado
    template_name = 'posts/post_search.html'

    # sobreescrevendo a query padrão do django
    def get_queryset(self):

        # obtendo o nome da categoria selecionada
        search_text = self.request.GET.get('s')

        # utilizando a qs já definida em PostIndex
        qs = super().get_queryset()

        # filtrando os resultados a partir do texto da busca
        # se o atributo titulo contiver o texto da busca
        # a partir da chave estrangeira id_autor, se o atibuto username da tabela User for igual o texto da busca
        # se o atributo conteudo contiver o texto da busca
        # se o atributo excerto contiver o texto da busca
        # a partir da chave estrangeira id_categoria, se o atibuto nome da tabela Categoria contiver o texto da busca
        qs = qs.filter(
            Q(titulo__icontains=search_text) |
            Q(id_autor__username__iexact=search_text) |
            Q(conteudo__icontains=search_text) |
            Q(excerto__icontains=search_text) |
            Q(id_categoria__nome__icontains=search_text)     
        )

        # retornando a query
        return qs


class PostCategory(PostIndex):

    # atribuindo o template a ser utilizado
    template_name = 'posts/post_category.html'

    # sobreescrevendo a query padrão do django
    def get_queryset(self):

        # obtendo o nome da categoria selecionada
        selected_category = self.kwargs.get('category', None)

        # utilizando a qs já definida em PostIndex
        qs = super().get_queryset()

        # filtrando os resultados
        # a partir da chave estrangeira id_categoria, utilizando o atributo nome da tabela Categoria como referência de comparação
        qs = qs.filter(id_categoria__nome__iexact=selected_category)

        # retornando a query
        return qs


class PostDetails(UpdateView):

    # atribuindo a model a ser utilizada
    model = Post

    # atribuindo o template a ser utilizado
    template_name = 'posts/post_details.html'

    # determinando o nome do objeto a ser passado ao template
    context_object_name = 'post'
    

    # sobreescrevendo a query padrão do django
    def get_queryset(self):

        # obtendo o id do post selecionada
        selected_post = self.kwargs.get('post', None)

        # chamando o método da superclasse
        qs = super().get_queryset()
      
        # filtrando por publicado=True e ordenando de forma decrescente por id
        qs = qs.filter(selected_post)

        # retornando a query
        return qs



# definindo a view loadtestdata
# tem a função de carregar uma massa de dados de teste
def loadtestdata(request):

    # criando os usuários
    for x in range(5):
        # cadastrando o novo usuario
        user = User.objects.create_user(username=f'usuario{x+1}', email=f'usuario{x+1}@email.com',
                                        password='123456', first_name=f'NomeUsuario{x+1}',
                                        last_name=f'SobrenomeUsuario{x+1}')
        user.save()

    # criando as categorias
    for x in range(5):
        # cadastrando a nova categoria
        categoria = Categoria.objects.create(nome=f'Categoria {x+1}')
        categoria.save()

    # criando os posts
    for x in range(30):

        # sorteando um usuário aleatório
        user = User.objects.get(id=random.randint(1, 5))

        # sorteando uma categoria aleatória
        categoria = Categoria.objects.get(id=random.randint(1, 5))

        # cadastrando o novo post
        post = Post.objects.create(titulo=f'Título do Post {x+1}', conteudo=f'Conteúdo do Post {x+1}',
                                   excerto=f'Excerto do Post {x+1}', publicado=True,
                                   id_autor=user, id_categoria=categoria)
        post.save()

    # criando os comentários
    for x in range(100):

        # sorteando um post aleatório
        post = Post.objects.get(id=random.randint(1, 30))

        # sorteando um usuário aleatório
        user = User.objects.get(id=random.randint(1, 5))

        # cadastrando o novo comentário
        comentario = Comentario.objects.create(nome=f'Título do Comentário {x+1}', email=f'comentario{x+1}@email.com',
                                               comentario=f'Text do Comentário {x+1}', publicado=True,
                                               id_post=post, id_autor=user)
        comentario.save()

    # redirecionando para a página de index
    return redirect('index')
