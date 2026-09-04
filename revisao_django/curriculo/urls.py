from os import name
from django.urls import path
from revisao_django.curriculo.views import index

urlpatterns = [
    path ('', index)
    
    
]