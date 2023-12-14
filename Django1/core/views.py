from django.shortcuts import redirect, render
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
    chaves = Chave.objects.filter(status=True)

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

def editar_chave(request, id):
    chave = Chave.objects.get(id=id)
    if request.method == 'POST':
        form = formChave(request.POST, instance=chave)
        if form.is_valid():
            form.save()
            return redirect('chaves')  # Redirecione para onde a lista de chaves é exibida
    else:
        form = formChave(instance=chave)

    return render(request, 'atualizachave.html', {'form': form})

def excluir_chave(request, id):
    chave = Chave.objects.get(id=id)
    chave.status = False
    print(chave.status)
    chave.save()
    return redirect('chaves')

def buscachave(request):
    busca = ''
    message = ''

    if 'busca' in request.GET:
        busca = request.GET['busca']
        if busca.strip():
            chave = Chave.objects.filter(nome__icontains=busca, status=True)
            if not chave:
                message = 'Nenhuma chave encontrada'
                chave = Chave.objects.filter(status = True)
            
        else:
            message = 'Campo de busca vazio'
            chave = Chave.objects.filter(status=True)
        
    return render(request, 'chaves.html', {'chaves': chave, 'message': message})    