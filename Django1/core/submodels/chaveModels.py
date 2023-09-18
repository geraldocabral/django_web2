from django.db import models
# Create your models here.
class Chave(models.Model):
    id = models.BigAutoField
    nome = models.CharField('Nome', max_length=100)
    situacao = models.BooleanField('Situação da chave', default=True)
    status = models.BooleanField('Status',  default=True)

    def __str__(self):
        return self.nome