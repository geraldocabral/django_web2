from django.urls import path

from .views import chaves, index, outro

from .subviews.servidorViews import servidor, servidores
from .subviews.insereChaveViews import inserechave

urlpatterns = [
    path('',index),
    path('outro',outro),
    path('servidor/<int:id>',servidor, name='servidorPorId'),
    path('chaves', chaves),
    path('inserechave', inserechave)
]