# Criar a view para chave
### Em core 
1. Primeiro é necessário fazer a importação do model da chave no arquivo views.py

- Import

from .models import Chave

1. Após isso definimos a requisição que será feita a busca das chaves existentes

-Codigo: 

def chaves(request):
    chaves = Chave.objects.all()
    context = {
        'chaves': chaves,
    }
    return render(request, 'chave.html', context)

1. agora o index

```
def index (request):
    chaves = Chave.objects.all()
    servidores = Servidor.objects.all()
    emprestimos = Emprestimo.objects.all()

    context = {
        'nome': 'Django 1',
        'chaves': chaves,
        'servidores': servidores,
        'emprestimos': emprestimos,
    }
    return render(request, 'index.html', context)
```


# Criar o caminho url utilizado para a página de chaves


1. Definir o path chaves no arquivo urls.py em core

-Criar o path dentro do urlpatterns
path('',index),
path('chaves', chaves)

1. EM django1

```
from .views import chaves, index, outro
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
]

LOGOUT_REDIRECT_URL = 'index'

```


# Criar o arquivo html que vai mostrar as chaves existentes
1. Em core, crie a paste templates

1. crie o arquivo index.html

1. em "core -> templates -> ```index.html``

```
 <h2> Chaves </h2>
        

        <h3><a href="chaves"> Visualizar chaves cadastradas</a></h3>
```

# Criar o arquivo html que vai mostrar as chaves existentes

1. Criar um novo arquivo com nome chaves.html, Em "core -> ``templates``"

1. Criar o código html que mostre a lista de chaves existentes


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