from django.shortcuts import render, redirect

# dependencias para possibilitar a utilização das Class Based Views
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# importando a model Post
from .models import Post
# importando a model Categoria
from categories.models import Categoria
# importando a model Comentario
from comments.models import Comentario
# importando a model User da área administrativa do django
from django.contrib.auth.models import User

# importando o formulario de Comentario
from comments.forms import FormComentario, FormComentarioLoggedUser

# dependências para querys complexas
from django.db.models import Q, Count, Case, When

# bilbioteca de mensagens do django
from django.contrib import messages

# biblioteca de números aleatórios
import random


# criando a view PostIndex
class PostIndex(ListView):

    # atribuindo a model a ser utilizada
    model = Post

    # atribuindo o template a ser utilizado
    template_name = 'posts/index.html'

    # definindo a quantidade de itens por página
    paginate_by = 6

    # determinando o nome do objeto a ser passado ao template
    context_object_name = 'posts'

    # sobreescrevendo o método do django de criação do contexto
    def get_context_data(self, **kwargs):

        # obtendo o contexto padrão da superclasse
        context = super().get_context_data(**kwargs)

        # obtendo as categorias cadastradas
        categories = Categoria.objects.all()

        # adicionando as categorias no contexto do template
        context['categories'] = categories

        return context

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


# criando a view PostSearch
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


# criando a view PostCategoria
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


# criando a view PostDetails
class PostDetails(UpdateView):

    # atribuindo a model a ser utilizada
    model = Post

    # atribuindo o template a ser utilizado
    template_name = 'posts/post_details.html'

    # determinando o nome do objeto a ser passado ao template
    # o template vai utilizar como referencia de consulta o atributo pk da URL
    context_object_name = 'post'

    # sobreescrevendo o método do django de criação do contexto
    def get_context_data(self, **kwargs):

        # obtendo o contexto padrão da superclasse
        context = super().get_context_data(**kwargs)

        # obtendo os dados do post atual
        post = self.get_object()

        # obtendo os comentários a serem publicados para o post
        comments = Comentario.objects.filter(publicado=True, id_post = post.id)

        # adicionando os comentarios no contexto do template
        context['comments'] = comments

        # obtendo as categorias cadastradas
        categories = Categoria.objects.all()

        # adicionando as categorias no contexto do template
        context['categories'] = categories

        return context

    # sobreescrevendo o método do django de seleção do formulário a ser apresentado
    def get_form_class(self):
        
        # se o usuário estiver logado
        if self.request.user.is_authenticated:
            # retorna o formulário só com o campo para comentário
            return FormComentarioLoggedUser
        else:
            # retorna o formulário com os campos para nome, email e comentário
            return FormComentario

    # sobreescrevendo o método do django de submissão do formulário
    def form_valid(self, form):

        # obtendo os dados do post atual
        post = self.get_object()

        # inserindo os dados do formulário em um objeto Comentario
        comentario = Comentario(**form.cleaned_data)

        # inserindo os dados do post no objeto formulário
        comentario.id_post = post

        # se o usuário estiver logado
        if self.request.user.is_authenticated:

            # inserindo os dados do usuário no objeto formulário
            comentario.nome = self.request.user.username
            comentario.email = self.request.user.email

        # salvando o comentário no BD
        comentario.save()

        # enviando mensagem de sucesso
        messages.success(self.request, 'Comentário enviado com sucesso.')

        # redirecionando para a página do post
        return redirect('post_details', pk=post.id)


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
    for x in range(10):
        # cadastrando a nova categoria
        categoria = Categoria.objects.create(nome=f'Categoria {x+1}')
        categoria.save()

    # criando os posts
    for x in range(30):

        # sorteando um usuário aleatório
        user = User.objects.get(id=random.randint(1, 5))

        # sorteando uma categoria aleatória
        categoria = Categoria.objects.get(id=random.randint(1, 10))

        # cadastrando o novo post
        post = Post.objects.create(titulo=f'Título do Post {x+1}', conteudo=f'Conteúdo do Post {x+1}',
                                   excerto=f'Excerto do Post {x+1}', publicado=True,
                                   id_autor=user, id_categoria=categoria)
        post.save()

    # criando os comentários
    for x in range(100):

        # sorteando um post aleatório
        post = Post.objects.get(id=random.randint(1, 30))

        # cadastrando o novo comentário
        comentario = Comentario.objects.create(nome=f'Comentador {x+1}', email=f'comentador{x+1}@email.com',
                                               comentario=f'Texto do Comentário {x+1}', publicado=True,
                                               id_post=post)
        comentario.save()

    # redirecionando para a página de index
    return redirect('index')
