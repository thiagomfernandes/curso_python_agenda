from django.shortcuts import render, get_object_or_404, redirect
from . models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.
def index(request):
    #contatos = Contato.objects.all() #get all objects / select * from app
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 3)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos' : contatos}) #passa como json

def detalhes(request, contato_id):
    try:
        contato = Contato.objects.get(id = contato_id)
        if not contato.mostrar:
            raise Exception('Usuário não pode ser acessado...')
        return render(request, 'contatos/detalhes.html', {'contato' : contato}) #passa como json

    except:
        messages.add_message(request, messages.constants.ERROR, 'Esse contato não existe ou não pode ser acessado...')
        return redirect('index')

    

def busca(request):
    termo = request.GET.get('termo')

    if not termo:
        messages.add_message(request, messages.constants.ERROR, 'Nenhum valor informado para a busca')
        return redirect('index')
    filtercampos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.order_by('-id').annotate(
        nomesobre = filtercampos
    ).filter(        
        Q(nomesobre__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True,
    )
    paginator = Paginator(contatos, 3)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos' : contatos})