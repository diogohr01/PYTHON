
from app_livraria import views
from django.urls import path

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('', views.login, name='login'),
    #livro
    path('livros', views.livros, name='livros'),  # Defina esta URL nomeada
    
    path('cadastro', views.signup, name='signup'),
    
]

