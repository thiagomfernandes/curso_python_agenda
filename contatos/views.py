from django.shortcuts import render, get_object_or_404
from . models import Contato
from django.core.paginator import Paginator
from django.http import Http404

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