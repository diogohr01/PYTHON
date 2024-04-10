
from django.urls import path
from . import views


urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('', views.login, name='login'),
    #livro
    path('livros/', views.livros, name='livros'),  # Defina esta URL nomeada
    
    path('cadastro/', views.signup, name='signup'),
    
    path('finalizar-sessao/', views.finalizar_sessao, name='finalizar_sessao'),
    
    path('criar_livro', views.criar_livro, name='criar_livro')    
    
]