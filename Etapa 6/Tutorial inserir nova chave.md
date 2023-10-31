3 Criar um arquivo formChave para receber os dados da chave a ser inserida dentro de core, de preferencia dentro de uma pasta exclusiva para forms

1. Fazer as importações necessárias

from django import forms

from ..submodels.chaveModels import Chave

2. Criar o form

class formChave(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Chave

		# specify fields to be used
		fields = [
			"nome"
		]



# Criar a view para inserir chave

1. Primeiro é necessário fazer a importação do model da chave e do form criado na etapa anterior

- Import

from ..submodels.chaveModels import Chave
from ..forms.formChave import formChave


2. Após isso definimos a requisição que será feita a busca das chaves existentes

-Codigo: 

def inserechave(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = formChave(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "inserechave.html", context)


# Criar o caminho url utilizado para a página de cadastrar chaves

1. Definir o path chaves no arquivo urls.py

-Criar o path dentro do urlpatterns

path('inserechave', inserechave)

# Criar o arquivo html que vai cadastrar as chaves

1. Criar um novo arquivo com nome inserechaves.html

2. Criar o código html que receba os dados e cadastre uma chave nova


<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta>
        <title>Nova chave</title>
    </head>
    <body style="display: flex; align-items: center; flex-direction: column;">
        <h1>Cadastrar nova chave</h1>
        <br>
        <form method="post" enctype="multipart/form-data" style="display: flex; flex-direction: column; width: 16.8%;">

            {% csrf_token %}

            {{ form.as_p}}

            <input type="submit" value="Submit">
        </form>
    </body>
</html>
