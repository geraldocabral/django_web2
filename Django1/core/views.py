from django.shortcuts import render
from .models import Chave, Servidor, Emprestimo

from .forms.formChave import formChave

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



def chaves(request):
    chaves = Chave.objects.all()

    context = {
        'chaves' : chaves
    }
    
    return render(request, 'chaves.html', context)
 
def inserechave(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = formChave(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_view.html", context)