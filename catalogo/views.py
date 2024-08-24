from django.http import HttpResponse
from django.shortcuts import render

from .models import Autor, Genero, Livro, Editora, Lingua, Copia, Emprestimo

# Create your views here.


def indexView(request):
    print('view:indexView')
     #contando objetos
    numAutores = Autor.objects.all().count()
    numlivros = Livro.objects.all().count()
    numcopias = Copia.objects.all().count()
    numGeneros = Genero.objects.all().count()
    numEditoras = Editora.objects.all().count()
    numLinguas = Lingua.objects.all().count()
    numEmprestimos  = Emprestimo.objects.all().count()


    # dicionario de variaveis de contexto
    contexto = {
        'numlivros' : numlivros,
        'numcopias' : numcopias,
        'numGeneros' : numGeneros,
        'numEditoras' : numEditoras,
        'numLinguas' : numLinguas,
        'numEmprestimos' : numEmprestimos,
    }


    return render(request, 'tlpindex.html', context=contexto)

