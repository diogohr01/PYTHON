
from django import forms
from django.db.models import fields
from .models import Livros
from django.db import models    
from datetime import date


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
    
    