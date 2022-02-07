from django.db import models


# criando a model de Categoria
class Categoria(models.Model):

    # criando o atributo nome como texto com tamanho máximo de 50
    nome = models.CharField(max_length=50, verbose_name='Nome')

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.nome
