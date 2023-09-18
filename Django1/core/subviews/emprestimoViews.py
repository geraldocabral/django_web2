from django.shortcuts import render
from submodels.emprestimoModels import Emprestimo

def emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    context = {
        'emprestimos': emprestimos,
    }
    return render(request, 'emprestimo.html', context)