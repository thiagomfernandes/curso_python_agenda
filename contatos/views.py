from django.shortcuts import render, get_object_or_404
from . models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all() #get all objects / select * from app
    return render(request, 'contatos/index.html', {'contatos' : contatos}) #passa como json

def detalhes(request, contato_id):
    #contato = Contato.objects.get(id = contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/detalhes.html', {'contato' : contato}) #passa como json