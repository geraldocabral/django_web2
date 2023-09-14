## Tutorial inicial front em Django
### Rotas

1. Em "core -> `views.py`" adicione a função:
    ``` python
    def index (request):
        return render(request, 'index.html')
    ```


1. Em "django1 -> ``urls.py``" 

    1. Importe:
        ```` python
        from django.urls import path, include
        ````
    1. Adicione em ``urlpatterns``:
        ````` python
        urlpatterns = [
            path('admin/', admin.site.urls),
            include('core.urls'),
        ] 
        `````

1. Em "core"
- Crie o arquivo ``urls.py``
    1. Importe:
        ````python
        from django.urls import path
        from .views import index
        ````
    1. Adicione:
        ```` python        
        urlpatterns = [
            path('',index),
        ]
        ````
### Templates
1. Em "django1 -> `setting.py` " 
    1. Em `TEMPLATES` vamos adicionar “templates” no DIRS do templates, para podermos fazer nossas paginas html. Ficando algo ssim:
    ``` python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```
1. Crie em "core" um diretório com o nome "templates"
    1. Neste novo diretorio crie o arquivo ``index.html``
    1. Em ``index.html`` adicione o conteudo:
        ``` html
        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta>
                <title> Organizar chaves - Index</title>
            </head>
            <body>
                <h1> Index </h1>
            </body>
        </html>
        ```
1. Iniciar o Servidor de Desenvolvimento para verificar se tudo esta funcionando corretamente.  
   >``python manage.py runserver``