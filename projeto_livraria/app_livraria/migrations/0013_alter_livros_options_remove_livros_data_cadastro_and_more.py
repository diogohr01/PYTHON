# Generated by Django 5.0.4 on 2024-04-11 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0012_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={},
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
    ]