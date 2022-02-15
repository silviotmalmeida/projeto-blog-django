from django.db import models
# importando a model User da área administrativa do django
from django.contrib.auth.models import User
# importando a model Post
from posts.models import Post
# importando a biblioteca de hora e data
from django.utils import timezone


# criando a model de Comentario
class Comentario(models.Model):

    # criando o atributo nome como texto com tamanho máximo de 150
    nome = models.CharField(max_length=150, verbose_name='Nome')

    # criando o atributo email como email
    email = models.EmailField(verbose_name='E-mail')

    # criando o atributo comentario como texto
    comentario = models.TextField(verbose_name='Comentário')

    # criando o atributo data como datetime atual
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')

    # criando o atributo publicado como booleano, com default False
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    # criando o atributo id_post com referência à model Post, com deleção em castaca
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')

    # criando o atributo id_autor com referência à model User, opcional, sem deleção em castaca
    # id_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Autor')

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.nome
