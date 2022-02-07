from django.db import models
# importando a model User da área administrativa do django
from django.contrib.auth.models import User
# importando a model Categoria
from categories.models import Categoria
# importando a biblioteca de hora e data
from django.utils import timezone


# criando a model de Post
class Post(models.Model):

    # criando o atributo titulo como texto com tamanho máximo de 255
    titulo = models.CharField(max_length=255, verbose_name='Título')

    # criando o atributo data como datetime atual
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')

    # criando o atributo conteudo como texto
    conteudo = models.TextField(verbose_name='Conteúdo')

    # criando o atributo excerto como texto 
    excerto = models.TextField(verbose_name='Excerto')

    # criando o atributo imagem, opcional, e definindo o destino do arquivo
    imagem = models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Imagem')

    # criando o atributo publicado como booleano, com default False
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    # criando o atributo id_autor com referência à model User, sem deleção em castaca
    id_autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')

    # criando o atributo id_categoria com referência à model Categoria, sem deleção em castaca, não obrigatória
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.titulo
