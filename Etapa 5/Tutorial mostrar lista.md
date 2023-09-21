from submodels.chaveModels import Chave

def chaves(request):
    chaves = Chave.objects.all()
    context = {
        'chaves': chaves,
    }
    return render(request, 'chave.html', context)


path('servidor/<int:id>',servidor, name='servidorPorId'),


        
        <h2> Chaves </h2>
        {% for chave in chaves %}
            <p> {{ chave }} </p>
        {% endfor %}