# Generated by Django 5.0.7 on 2024-08-17 17:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idAutor', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45, verbose_name='Nome do Autor')),
                ('dtNascimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('idEditora', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45, verbose_name='Editora')),
                ('endereco', models.TextField(verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=10, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.BigAutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=45, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Lingua',
            fields=[
                ('idLingua', models.BigAutoField(primary_key=True, serialize=False)),
                ('lingua', models.CharField(max_length=45, verbose_name='Lingua')),
            ],
        ),
        migrations.CreateModel(
            name='Copia',
            fields=[
                ('idCopia', models.BigAutoField(primary_key=True, serialize=False)),
                ('dtEntrada', models.DateField(verbose_name='Data de Entrada')),
                ('editora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.editora')),
                ('lingua', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.lingua')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('idEmprestimo', models.BigAutoField(primary_key=True, serialize=False)),
                ('dtEmprestimo', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Emprestimo')),
                ('dtDevolucao', models.DateField(blank=True, null=True, verbose_name='Data de Devolução')),
                ('copia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogo.copia')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('idLivro', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo do Livro')),
                ('sumario', models.TextField(verbose_name='Sumario')),
                ('ISBN', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('dtPublicacao', models.DateField(verbose_name='Data de Publicação')),
                ('autor', models.ManyToManyField(related_name='livros', to='catalogo.autor')),
                ('genero', models.ManyToManyField(related_name='livros', to='catalogo.genero')),
            ],
        ),
        migrations.AddField(
            model_name='copia',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogo.livro'),
        ),
    ]
