# Generated by Django 5.0.4 on 2024-04-11 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0010_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
