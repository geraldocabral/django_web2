# Criar as views de edição e exclusão
### Em views.py

1. Criar as def para editar uma chave e para excluir uma chave

```
def editar_chave(request, id):
    chave = Chave.objects.get(id=id)
    if request.method == 'POST':
        form = formChave(request.POST, instance=chave)
        if form.is_valid():
            form.save()
            return redirect('chaves')  # Redirecione para onde a lista de chaves é exibida
    else:
        form = formChave(instance=chave)

    return render(request, 'atualizachave.html', {'form': form})

def excluir_chave(request, id):
    chave = Chave.objects.get(id=id)
    chave.status = False
    print(chave.status)
    chave.save()
    return redirect('chaves')

```

# Definir os caminhos utilizados para editar e excluir
### Arquivo urls.py dentro da pasta core

1. Definir o path editar_chave e excluir_chave.

Os paths ficam dessa maneira:

```
urlpatterns = [
    path('',index, name='index'),
    path('outro',outro),
    path('servidor/<int:id>',servidor, name='servidorPorId'),
    path('chaves', chaves, name='chaves'),
    path('inserechave', inserechave),
    path('chave/editar/<int:id>/', editar_chave, name='editar_chave'),
    path('chave/excluir/<int:id>/',excluir_chave, name='excluir_chave'),
]

```


# Alterar o arquivo html que mostra as chaves para adicionar os botões de edição e exclusão.
### Arquivo chaves.html

1. Adicionar os botões de edição e exlcusão no arquivo html, e adicionar estilos css 

```
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Chaves</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        .link-icons {
            margin: 0 10px;
        }
        /* Increase spacing between rows and columns */
        td {
            padding: 20px; /* Increase as needed */
            width: 300px; /* Increase as needed */
            height: 100px; /* Increase as needed */
        }
        tr {
            margin: 20px 0; /* Increase as needed */
        }
        /* Add a flex container for the key name and icons */
        .key-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px; /* Increase as needed */
            border-bottom: 1px solid #000; /* Add a bottom border */
            padding-bottom: 10px; /* Add some padding to space out the border */
        }
        .btn-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px; /* Add some top margin */
        }
    </style>
</head>
<body >
    <table style="display: flex; justify-content: center; margin-top: 250px; ">
        <tr>
            <th style="border-style: groove; width: 250px; background-color: lightgray;"><h1>Chaves</h1></th>
        </tr>
        <tr>
            <td style="border-style: groove; font-size: large;">
                {% for chave in chaves %}
                
                    <!-- Wrap the key name and icons in a flex container -->
                    <div class="key-item">
                        <span>{{ chave }}</span>
                        <div>
                            <a class="link-icons" href="{% url 'editar_chave' id=chave.id %}">
                                <i class="fas fa-edit"></i>
                            </a>
                            |
                            <a class="link-icons" href="{% url 'excluir_chave' id=chave.id %}">
                                <i class="fas fa-trash"></i>
                            </a>
                        </div>
                    </div>
                {% endfor %}
            </td>
            
        </tr>
    </table>
    <div class="btn-container">
        <a href="{% url 'index' %}" class="btn">Voltar para página inicial</a>
    </div>
    
</body>
</html>
</body>
    
        
</html>

```

# Criar o arquivo html de editar chave
### Dentro de templates

1. criar um arquivo com o nome atualizachave.html e usar o seguinte codigo:

```
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Editar Chave</title>
    </head>
    <body style="display: flex; align-items: center; flex-direction: column;">
        <h1>Editar Chave</h1>
        <br>
        <form method="post" enctype="multipart/form-data" style="display: flex; flex-direction: column; width: 16.8%;">

            {% csrf_token %}

            {{ form.as_p }}

            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

# Rodar o projeto e acessar a url para verificar o funcionamentp
### no console dentro de Django1

```
python manage.py runserver

```

http://127.0.0.1:8000/