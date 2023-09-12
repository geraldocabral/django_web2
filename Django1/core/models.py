from django.db import models

# Create your models here.
class Chave(models.Model):
    id = models.AutoField
    nome = models.CharField('Nome', max_length=100)
    situacao = models.BooleanField('Situação da chave')
    status = models.BooleanField('Status')

class Servidor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF',max_length=15)
    contato = models.CharField('Contato do servidor',max_length=15)
    nascimento = models.DateField('Data de Nascimento')
    status = models.BooleanField('Status')

class Emprestimo(models.Model):
    dataHoraEmprestimo = models.DateTimeField('Hora Emprestimo')
    dataHoraDevolucao = models.DateTimeField('Hora Devolução')
    status = models.BooleanField('Status')


