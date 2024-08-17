from django.db import models
from django.utils import timezone


# Create your models here.


# Classe que representa um livro (não a copia do livro)


class Autor(models.Model):
    idAutor = models.BigAutoField(primary_key=True)
    nome = models.CharField(verbose_name="Nome do Autor", max_length=45, null=False, blank=False) 
    dtNascimento = models.DateField(verbose_name="Data de Nascimento")
    
    def __str__(self):
        return f"id: {self.idAutor} - nome: {self.nome}"


class Genero(models.Model):
    idGenero = models.BigAutoField(primary_key=True)
    genero = models.CharField(verbose_name="Genero", max_length=45, null=False, blank=False) 


    def __str__(self):
        return f"id: {self.idGenero} - genero: {self.genero}"


class Livro(models.Model):
    idLivro = models.BigAutoField(primary_key=True)
    titulo = models.CharField(verbose_name="Titulo do Livro", max_length=100, null=False, blank=False)
    sumario = models.TextField(verbose_name="Sumario")
    ISBN = models.CharField(verbose_name="ISBN", max_length=13, null=False, blank=False, unique=True)
    dtPublicacao = models.DateField(verbose_name="Data de Publicação")
    # um livro pode ter muitos autores e um autor pode escrever muitos livros (n:n)
    autor = models.ManyToManyField(Autor, related_name='livros')
    # um livro pode ter muitos generos e um genero está associdado a muitos livros (n:n)
    genero = models.ManyToManyField(Genero, related_name='livros')
    def __str__(self):
        return f"id: {self.idLivro} - titulo: {self.titulo}"


class Editora(models.Model):
    idEditora = models.BigAutoField(primary_key=True)
    nome = models.CharField(verbose_name="Editora", max_length=45, null=False, blank=False)
    endereco = models.TextField(verbose_name="Endereço", null=False, blank=False)
    telefone = models.CharField(verbose_name="Telefone", max_length=10, null=False, blank=False)


    def __str__(self):
        return f"id: {self.idEditora} - nome: {self.nome}"    


class Lingua(models.Model):
    idLingua = models.BigAutoField(primary_key=True)
    lingua = models.CharField(verbose_name="Lingua", max_length=45, null=False, blank=False)


    def __str__(self):
        return f"id: {self.idLingua} - lingua: {self.lingua}"      


class Copia(models.Model):
    idCopia = models.BigAutoField(primary_key=True)
    dtEntrada = models.DateField(verbose_name="Data de Entrada")
    livro = models.ForeignKey(Livro,on_delete=models.PROTECT)
    editora = models.ForeignKey(Editora,null=True,on_delete=models.SET_NULL)
    lingua = models.ForeignKey(Lingua,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return f"id: {self.idCopia} - data entrada: {self.dtEntrada}"      


class Emprestimo(models.Model):
    idEmprestimo = models.BigAutoField(primary_key=True)
    dtEmprestimo = models.DateField(verbose_name="Data de Emprestimo",default=timezone.now)
    dtDevolucao = models.DateField(verbose_name="Data de Devolução", null=True, blank=True)
    copia = models.ForeignKey(Copia,on_delete=models.PROTECT)


    def __str__(self):
        return f"id: {self.idEmprestimo} - data emprestimo: {self.dtEmprestimo}"
