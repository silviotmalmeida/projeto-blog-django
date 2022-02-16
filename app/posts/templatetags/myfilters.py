# arquivo com filtros personalizados criados para a utilização nos templates

# importação default
from django import template


# criando o decorador a ser utilizado nos filtros
register = template.Library()


# criando o filtro reponsável por ajustar o termo "Comentário" no singular ou plural
# decorando a função como um filtro chamado plural_comentarios
@register.filter(name='plural_comentarios')
# criando a função
# o argumento a ser recebido é o texto antes do pipe
def plural_comentarios(num_comentarios):

    # tratando exceções
    try:

        # obtendo o número de comentários em inteiro
        num_comentarios = int(num_comentarios)

        # se não houver comentários:
        if num_comentarios == 0:
            # exibe o texto 'Nenhum comentário'
            return f'Nenhum comentário'

        # se existir somente um comentário
        elif num_comentarios == 1:
            # exibe o texto no singular
            return f'{num_comentarios} comentário'

        # senão:
        else:
            # exibe o texto no plural
            return f'{num_comentarios} comentários'

    # em caso de exceção
    except:
        # exibe o texto de forma genérica
        return f'{num_comentarios} comentário(s)'
