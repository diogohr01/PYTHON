# Generated by Django 5.0.4 on 2024-04-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_livraria', '0003_usuario_delete_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(max_length=128),
        ),
    ]
