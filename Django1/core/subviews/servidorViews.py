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
        servidorNovo = Servidor()
        servidorNovo.nome = request.POST.get('nome')
        servidorNovo.cpf = request.POST.get('cpf')
        servidorNovo.contato = request.POST.get('contato')
        servidorNovo.nascimento = request.POST.get('nascimento')
        servidorNovo.status = True
        servidor.save(servidorNovo)
    return render(request, 'servidorPost.html')