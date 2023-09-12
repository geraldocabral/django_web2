from django.urls import path

from .views import index, outro

urlpatterns = [
    path('',index),
    path('outro',outro),
]