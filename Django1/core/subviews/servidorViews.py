from django.shortcuts import render
from core.models import Servidor

def servidores(request):
    servidores = Servidor.objects.all()
    context = {
        'servidores': servidores,
    }
    return render(request, 'servidores.html', context)

def servidor(request, id):
    servidor = Servidor.objects.get(id=id) #sim id=id, um id é o tipo do get e o segundo é o valor
    context = {
        'servidor': servidor,
    }
    return render(request, 'servidor.html', context)