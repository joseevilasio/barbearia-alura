from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto

# Create your views here.


def index(request):    
    return render(request, 'index.html')

def produtos(request):

    produtos = Produto.objects.all()
    
    dados = {
        'produtos': produtos
    }

    return render(request, 'produtos.html', dados)

def contatos(request):
    return render(request, 'contatos.html')