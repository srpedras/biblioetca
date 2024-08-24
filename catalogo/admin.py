from django.contrib import admin
from .models import Autor, Genero, Livro, Editora, Lingua, Copia, Emprestimo


# Register your models here.


admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Livro)
admin.site.register(Editora)
admin.site.register(Lingua)
admin.site.register(Copia)
admin.site.register(Emprestimo)
