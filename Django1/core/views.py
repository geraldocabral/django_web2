from django.shortcuts import render
from .models import Chave, Servidor, Emprestimo

# Create your views here.
def index (request):
    chaves = Chave.objects.all()
    servidores = Servidor.objects.all()
    emprestimos = Emprestimo.objects.all()

    context = {
        'nome': 'Django 1',
        'chaves': chaves,
        'servidores': servidores,
        'emprestimos': emprestimos,
    }
    return render(request, 'index.html', context)

def outro(request):
    return render(request, 'outro.html')