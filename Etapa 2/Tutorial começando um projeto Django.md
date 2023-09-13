# Tutorial começando um projeto Django
## Tutorial criação de projeto Django

1. Criar um Novo Projeto Django

    Você pode criar um novo projeto Django usando o comando `django-admin` ou `manage.py`. Vamos usar `django-admin` para criar um projeto chamado "DJango1":

    >````django-admin startproject Django1 .````

    Este comando criará um diretório chamado "DJango1" com a estrutura inicial do projeto.
    Use o `.` para cria-lo na pasta em que esta no momento

1. Configurar o Banco de Dados

    Abra o arquivo `settings.py` dentro do diretório "meuprojeto" e vá até a seção `DATABASES` se quiser modificar e configurar as informações de conexão com o banco de dados. Por padrão:

    ```` python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite por padrão
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Caminho para o arquivo do banco de dados
        }
    }
    ````


## Tutorial criação de um aplicativo Django
1. Criar um Aplicativo


    Os projetos Django podem ser compostos por vários aplicativos. Um aplicativo é uma parte específica de funcionalidade em seu projeto. Vamos criar um aplicativo chamado "core":

    >``django-admin startapp core``

1. Em "django1 -> `setting.py` " 
    1. Em `INSTALLED_APPS` vamos adicionar nossa aplicação, ficando algo assim: 
    ``` python
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
    ]
    ```

1. Iniciar o Servidor de Desenvolvimento

    Para testar seu projeto localmente, execute o seguinte comando para iniciar o servidor de desenvolvimento do Django:

   >``python manage.py runserver``

    Acesse seu projeto, por padrão, em http://localhost:8000/ no seu navegador.

    No terminal ira aparecer algo assim:
    ```
    PS C:\..\Django1> python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...
        System check identified no issues (0 silenced).
        You have 18 unapplied migration(s). Your project may not work
        properly until you apply the migrations for app(s): admin, auth,
        contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        September 11, 2023 - 22:50:45
        Django version 4.2.5, using settings 'django1.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK
    ```

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