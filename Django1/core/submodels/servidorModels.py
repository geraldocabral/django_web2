from django.db import models

class Servidor(models.Model):
    id = models.BigAutoField
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF',max_length=15)
    contato = models.CharField('Contato do servidor',max_length=15)
    nascimento = models.DateField('Data de Nascimento')
    status = models.BooleanField('Status', default=True)

    def __str__(self):
        return self.nome