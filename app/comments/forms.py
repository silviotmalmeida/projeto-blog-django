from django.forms import ModelForm

# importando a model Comentario
from .models import Comentario


# definindo o formulário
class FormComentario(ModelForm):

    # sobreescrevendo o método de validação do formulário
    def clean(self):

        # obtém os dados do formulário
        form_data = self.cleaned_data

        name = form_data.get('nome')
        email = form_data.get('email')
        comment = form_data.get('comentario')

        # inserindo validações personalizadas
        if len(name) < 5:
            self.add_error(
                'nome',
                'O nome precisa ter ao menos 5 caracteres.'
            )

        if len(comment) < 15:
            self.add_error(
                'comentario',
                'O comentário precisa ter ao menos 15 caracteres.'
            )

    # definindo a estrutura do formulário
    class Meta:

        # definindo a model do formulário
        model = Comentario

        # definindo os campos a serem considerados
        fields = ('nome', 'email', 'comentario')