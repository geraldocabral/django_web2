from django.urls import path

from .views import chaves, index, outro, editar_chave, excluir_chave

from .subviews.servidorViews import servidor, servidores
from .subviews.insereChaveViews import inserechave

urlpatterns = [
    path('',index, name='index'),
    path('outro',outro),
    path('servidor/<int:id>',servidor, name='servidorPorId'),
    path('chaves', chaves, name='chaves'),
    path('inserechave', inserechave),
    path('chave/editar/<int:id>/', editar_chave, name='editar_chave'),
    path('chave/excluir/<int:id>/',excluir_chave, name='excluir_chave'),
]