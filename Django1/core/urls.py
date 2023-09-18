from django.urls import path

from .views import index, outro

from .subviews.servidorViews import servidor, servidores

urlpatterns = [
    path('',index),
    path('outro',outro),
    path('servidor/<int:id>',servidor, name='servidor'),
]