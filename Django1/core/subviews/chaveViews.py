from django.shortcuts import render
from submodels.chaveModels import Chave

def chaves(request):
    chaves = Chave.objects.filter(status=True)
    context = {
        'chaves': chaves,
    }
    return render(request, 'chaves.html', context)