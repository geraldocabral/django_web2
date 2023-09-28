# Criar a view para chave

1. Primeiro é necessário fazer a importação do model da chave no arquivo views.py

- Import

from .models import Chave

2. Após isso definimos a requisição que será feita a busca das chaves existentes

-Codigo: 

def chaves(request):
    chaves = Chave.objects.all()
    context = {
        'chaves': chaves,
    }
    return render(request, 'chave.html', context)


# Criar o caminho url utilizado para a página de chaves

1. Definir o path chaves no arquivo urls.py

-Criar o path dentro do urlpatterns

path('chaves', chaves)

# Criar o arquivo html que vai mostrar as chaves existentes

1. Criar um novo arquivo com nome chaves.html

2. Criar o código html que mostre a lista de chaves existentes


<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Chaves</title>
</head>
<body >
    <table style="display: flex; justify-content: center; margin-top: 250px; ">
        <tr>
            <th style="border-style: groove; width: 250px; background-color: lightgray;"><h1>Chaves</h1></th>
        </tr>
        <tr>
            <th style="border-style: groove; font-size: large;">
                {% for chave in chaves %}
                    <p> {{ chave }} </p>
                {% endfor %}
            </th>
        </tr>
    </table>
</body>
    
        
</html>