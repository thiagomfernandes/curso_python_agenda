from django.shortcuts import render, get_object_or_404
from . models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat

# Create your views here.
def index(request):
    #contatos = Contato.objects.all() #get all objects / select * from app
    contatos = Contato.objects.order_by('-id').filter(mostrar=True)
    paginator = Paginator(contatos, 3)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos' : contatos}) #passa como json

def detalhes(request, contato_id):
    contato = Contato.objects.get(id = contato_id)
    #contato = get_object_or_404(Contato, id=contato_id)
    if not contato or not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/detalhes.html', {'contato' : contato}) #passa como json

def busca(request):
    termo = request.GET.get('termo')

    if not termo:
        termo= ''

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