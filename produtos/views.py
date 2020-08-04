from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto, Contatos

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
    if request.method == 'POST':
        form = Contatos()
        form.nome = request.POST['nome']
        form.email = request.POST['email']
        form.telefone = request.POST['telefone']
        form.mensagem = request.POST['mensagem']
        form.contato = request.POST['contato']
        form.turno_atendimento = request.POST['turno_atendimento']
        
        if request.POST['newsletter'] == "on":
            form.newsletter = True
        else:
            form.newsletter = False

        form.save()
        
        return redirect('index')
    else:
        return render(request, 'contatos.html')
