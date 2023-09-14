from django.db import models

# Create your models here.
class Chave(models.Model):
    id = models.AutoField
    nome = models.CharField('Nome', max_length=100)
    situacao = models.BooleanField('Situação da chave', default=True)
    status = models.BooleanField('Status',  default=True)

    def __str__(self):
        return self.nome

class Servidor(models.Model):
    id = models.AutoField
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF',max_length=15)
    contato = models.CharField('Contato do servidor',max_length=15)
    nascimento = models.DateField('Data de Nascimento')
    status = models.BooleanField('Status', default=True)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    id = models.AutoField
    dataHoraEmprestimo = models.DateTimeField('Hora Emprestimo')
    dataHoraDevolucao = models.DateTimeField('Hora Devolução', null=True, blank=True)
    status = models.BooleanField('Status', default=True)
    chaveEmprestada = models.ForeignKey(Chave, on_delete=models.CASCADE, to_field='id', related_name='chaveEmprestimo')
    servidorEmprestimo = models.ForeignKey(Servidor, on_delete=models.CASCADE, to_field='id', related_name='servidorEmprestimo')
    servidorDevolucao = models.ForeignKey(Servidor, on_delete=models.CASCADE, to_field='id', related_name='servidorDevolucao', null=True, blank=True)


