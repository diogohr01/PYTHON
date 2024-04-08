from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128) 
    nome = models.TextField(max_length=255)