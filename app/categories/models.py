from django.db import models


# criando a model de Category
class Category(models.Model):

    # criando o atributo name como texto com tamanho máximo de 50
    name = models.CharField(max_length=50)

    # definindo qual atributo da model será exibido na área administrativa
    def __str__(self):
        return self.name
