# importação default
from django.forms import ModelForm

# importando a model Comentario
from .models import Comentario

# biblioteca de requisições http
import requests


# definindo o formulário para usuários não logados
class FormComentario(ModelForm):

    # sobreescrevendo o método de validação do formulário
    def clean(self):

        # obtém os dados crus do formulário
        raw_form_data = self.data

        # obtém a resposta do recaptcha do formulário
        recaptcha_response = raw_form_data.get('g-recaptcha-response')

        # se o recaptcha não tiver sido marcado
        if not recaptcha_response:

            # envia mensagem de erro
            self.add_error(
                'comentario',
                'Por favor marque a opção "Não sou um robô".'
            )
            return

        # senão
        else:

            # fazendo a requisição para validação do recaptcha
            recaptcha_request = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': '6Ldq7ogeAAAAAJJE0bLLRGutXZBgl7yzaaCM5kro',
                    'response': recaptcha_response
                }
            )

            # obtendo os dados de retorno
            recaptcha_result = recaptcha_request.json()

            # se a validação não for bem sucedida
            if not recaptcha_result.get('success'):
                # envia mensagem de erro
                self.add_error(
                    'comentario',
                    'Validação sem sucesso.'
                )
                return

            # senão
            else:
        
                # obtém os dados limpos do formulário
                cleaned_form_data = self.cleaned_data

                # obtendo os dados inseridos
                name = cleaned_form_data.get('nome')
                email = cleaned_form_data.get('email')
                comment = cleaned_form_data.get('comentario')

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


# definindo o formulário para usuários logados
class FormComentarioLoggedUser(ModelForm):

    # sobreescrevendo o método de validação do formulário
    def clean(self):

        # obtém os dados crus do formulário
        raw_form_data = self.data

        # obtém a resposta do recaptcha do formulário
        recaptcha_response = raw_form_data.get('g-recaptcha-response')

        # se o recaptcha não tiver sido marcado
        if not recaptcha_response:

            # envia mensagem de erro
            self.add_error(
                'comentario',
                'Por favor marque a opção "Não sou um robô".'
            )
            return

        # senão
        else:

            # fazendo a requisição para validação do recaptcha
            recaptcha_request = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                    'secret': '6Ldq7ogeAAAAAJJE0bLLRGutXZBgl7yzaaCM5kro',
                    'response': recaptcha_response
                }
            )

            # obtendo os dados de retorno
            recaptcha_result = recaptcha_request.json()

            # se a validação não for bem sucedida
            if not recaptcha_result.get('success'):
                # envia mensagem de erro
                self.add_error(
                    'comentario',
                    'Validação sem sucesso.'
                )
                return

            # senão
            else:
        
                # obtém os dados limpos do formulário
                cleaned_form_data = self.cleaned_data

                # obtendo os dados inseridos
                comment = cleaned_form_data.get('comentario')

                # inserindo validações personalizadas
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
        fields = ('comentario',)
