from django.shortcuts import render
from submodels.chaveModels import Chave

def chaves(request):
    chaves = Chave.objects.all()
    context = {
        'chaves': chaves,
    }
    return render(request, 'chave.html', context)