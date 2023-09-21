1. Criar super usuario
    >`python manage.py createsuperuser`

Usuário: admin
Endereço de email: admin@admin.com
Password: admin

Agora em localhost:8000/admin teremos acesso a area administrativa do django

1. Em "core -> `admin.py`"
    1. Importe: 
        ``` python
            from .models import Chave, Emprestimo, Servidor 
        ```
    1. Registrando as classes
        ``` python
            admin.site.register(Chave)
            admin.site.register(Emprestimo)
            admin.site.register(Servidor)
        ```
    1. Verifique se a aplicação esta rodando corrPPetamente, e enrtre em localhost:8000/admin

1. Em "core -> `models.py`"
    1. Criar dentro das classes ``Sevidor`` e ``Chave`` a seguinte função:
        ``` python
        def __str__(self):
            return self.nome
        ```
1. Em "core -> `admin.py`"
    1. Criar dentro as sequintes classes
        ``` python
        class EmprestimoAdmin(admin.ModelAdmin):
            list_display = ('dataHoraEmprestimo', 'dataHoraDevolucao')

        class ChaveAdmin(admin.ModelAdmin):
            list_display = ('nome', 'situacao')

        class ServidorAdmin(admin.ModelAdmin):
            list_display = ('nome', 'contato', 'cpf', 'nascimento')
        ```
    1. Registre estas classes igual feito anteriormente, ficando:
        ``` python django
        admin.site.register(Chave,  ChaveAdmin)
        admin.site.register(Emprestimo, EmprestimoAdmin)
        admin.site.register(Servidor, ServidorAdmin)  
        ```

1. Se desejar altere o caminho padrão da area
    1. Em "django1 -> ``urls.py``"
        altere para o que desejar