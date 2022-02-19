# dependencia default
from django.db import models
# importando a model User da área administrativa do django
from django.contrib.auth.models import User
# importando a model Categoria
from categories.models import Categoria
# importando a biblioteca de hora e data
from django.utils import timezone
# importando o pillow para processamento de imagens
from PIL import Image
# obtendo os dados do app definidos no settings
from django.conf import settings
# importando a biblioteca de navegação de arquivos
import os


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
    imagem = models.ImageField(
        blank=True, upload_to='pictures/%Y/%m/', verbose_name='Imagem')

    # criando o atributo publicado como booleano, com default False
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    # criando o atributo id_autor com referência à model User, sem deleção em castaca
    id_autor = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')

    # criando o atributo id_categoria com referência à model Categoria, sem deleção em castaca, não obrigatória
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.titulo

    # sobrescrevendo o método do django de salvar no BD
    def save(self, *args, **kwargs):

        # utilizando as definições da superclasse
        super().save(*args, **kwargs)
        
        if self.imagem:

            # processando a imagem submetida
            self.resize_image(self.imagem, 800)

    # criando método estático para processamento da imagem do post
    @staticmethod
    def resize_image(image_name, new_width):

        # obtendo o caminho da imagem
        img_path = os.path.join(settings.MEDIA_ROOT, str(image_name))

        # obtendo os dados da imagem original
        original_image = Image.open(img_path)
        width, height = original_image.size

        # se o comprimento da imagem for menor ou igual ao novo comprimento
        if width <= new_width:
            # fecha a imagem
            original_image.close()
        else:
            # calculando a nova altura
            new_height = round((new_width * height)/width)
            # criando a nova imagem
            new_image = original_image.resize(
                (new_width, new_height), Image.ANTIALIAS)
            # salvando a nova imagem otimizada no lugar da original
            new_image.save(img_path, optimize=True, quality=60)
            # fechando a imagem
            new_image.close()
