from django.db import models
from .chaveModels import Chave
from .servidorModels import Servidor

# Create your models here.
class Emprestimo(models.Model):
    id = models.AutoField
    dataHoraEmprestimo = models.DateTimeField('Hora Emprestimo')
    dataHoraDevolucao = models.DateTimeField('Hora Devolução', null=True, blank=True)
    status = models.BooleanField('Status', default=True)
    chaveEmprestada = models.ForeignKey(Chave, on_delete=models.CASCADE, to_field='id', related_name='chaveEmprestimo')
    servidorEmprestimo = models.ForeignKey(Servidor, on_delete=models.CASCADE, to_field='id', related_name='servidorEmprestimo')
    servidorDevolucao = models.ForeignKey(Servidor, on_delete=models.CASCADE, to_field='id', related_name='servidorDevolucao', null=True, blank=True)

    def __str__(self):
        return self.chaveEmprestada.nome + ' | ' + self.servidorEmprestimo.nome
