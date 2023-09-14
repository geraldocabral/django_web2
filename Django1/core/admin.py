from django.contrib import admin

from .models import Chave, Emprestimo, Servidor


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('chaveEmprestada' ,'dataHoraEmprestimo', 'dataHoraDevolucao')

class ChaveAdmin(admin.ModelAdmin):
    list_display = ('nome', 'situacao')

class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'cpf', 'nascimento')

# Register your models here.
admin.site.register(Chave,  ChaveAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Servidor, ServidorAdmin)  