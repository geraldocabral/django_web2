from django.shortcuts import render
from core.submodels.emprestimoModels import Emprestimo

def emprestimo(request):
    emprestimos = Emprestimo.objects.all()
    context = {
        'emprestimos': emprestimos,
    }
    return render(request, 'emprestimo.html', context)