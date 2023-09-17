from django.shortcuts import render
from core.submodels.chaveModels import Chave

def chaves(request):
    chaves = Chave.objects.all()
    context = {
        'chaves': chaves,
    }
    return render(request, 'chave.html', context)