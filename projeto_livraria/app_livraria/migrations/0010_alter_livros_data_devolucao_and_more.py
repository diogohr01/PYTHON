# Generated by Django 5.0.4 on 2024-04-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0009_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
    ]