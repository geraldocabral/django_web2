from django.shortcuts import render
from core.models import Servidor
from django.shortcuts import get_object_or_404 # se o cara for mexer na url

def servidores(request):
    servidores = Servidor.objects.all()
    context = {
        'servidores': servidores,
    }
    return render(request, 'servidores.html', context)

def servidor(request, id):
    #servidor = Servidor.objects.get(id=id) #sim id=id, um id é o tipo do get e o segundo é o valor
    servidor = get_object_or_404(Servidor, id=id) #sim id=id, um id é o tipo do get e o segundo é o valor
    context = {
        'servidor': servidor,
    }
    return render(request, 'servidor.html', context)

def servidorPost(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        contato = request.POST.get('contato')
        nascimento = request.POST.get('nascimento')
        status = True
        
        servidor.save()
    return render(request, 'servidorPost.html')