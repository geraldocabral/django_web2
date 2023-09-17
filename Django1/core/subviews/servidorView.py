from django.shortcuts import render
from core.submodels.servidorModels import Servidor

def servidores(request):
    servidores = Servidor.objects.all()
    context = {
        'servidores': servidores,
    }
    return render(request, 'servidor.html', context)

def servidor(request, id):
    servidor = Servidor.objects.get(id=id)
    context = {
        'servidor': servidor,
    }
    return render(request, 'servidor.html', context)