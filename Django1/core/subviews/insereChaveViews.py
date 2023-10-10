from django.shortcuts import render
 
from ..submodels.chaveModels import Chave
from ..forms.formChave import formChave

 
 
def inserechave(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = formChave(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "inserechave.html", context)