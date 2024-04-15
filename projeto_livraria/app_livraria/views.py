from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Livros
from hashlib import sha256
from .forms import CadastroLivro
from django.utils import timezone
from django.urls import reverse
import openai


def login(request):
    if request.method == 'GET':
        cache.clear()
        return render(request, 'index.html')  # Renderiza o formulário de login

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        # Autentica o usuário
        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            # Se as credenciais forem válidas, realiza o login
            login_django(request, user)
            return render(request, 'index.html', {'logado': True})  # Redireciona para a página de login após o cadastro
  # Redireciona para a página 'livros' após o login
        else:
            # Se as credenciais forem inválidas, exibe uma mensagem de erro
            messages.error(request, 'Credenciais inválidas. Por favor, tente novamente.')
            return redirect('login')  # Redireciona de volta para a página de login




def signup(request):
    if request.method == 'GET':
        cache.clear()
        # Remove a variável cadastrado da sessão se existir
        if 'cadastrado' in request.session:
            del request.session['cadastrado']
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmaSenha')
        
        
        # Lista para armazenar mensagens de erro
        erros = []
        
        # Verifica se todos os campos foram preenchidos
        if not username:
            erros.append('Por favor, preencha o nome de usuário.')
        if not email:
            erros.append('Por favor, preencha o email.')
        if not senha:
            erros.append('Por favor, preencha a senha.')
        if not confirma_senha:
            erros.append('Por favor, confirme a senha.')
        
        # Verifica se as senhas coincidem
        if senha != confirma_senha:
            erros.append('As senhas não coincidem.')
        
        # Verifica se o username e email já existem
        existing_user = User.objects.filter(username=username).exists()
        existing_email = User.objects.filter(email=email).exists()
        
        if existing_user:
            erros.append('Este nome de usuário já está em uso. Por favor, escolha outro.')
        if existing_email:
            erros.append('Este email já está em uso. Por favor, escolha outro.')
        
        if erros:
            # Se houver erros, exibe as mensagens de erro e redireciona de volta para o formulário
            for erro in erros:
                messages.error(request, erro)
            return redirect('signup')
        else:
            # Se não houver erros, cria o novo usuário
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
                      
            
            return render(request, 'signup.html', {'cadastrado': True})  # Redireciona para a página de login após o cadastro
 
 
@login_required

def livros(request):
    if request.method == 'GET':
        cache.clear()
        form = CadastroLivro()
        livros = Livros.objects.all().filter(emprestado=False)
        livros_alugados = Livros.objects.all().filter(emprestado=True)   
        return render(request, 'livros.html', {'form': form, 
                                               'user': request.user, 
                                               'is_superuser': request.user.is_superuser, 
                                               'livros': livros,
                                               'livros_alugados': livros_alugados})
            


def finalizar_sessao(request):
    # Limpa todos os dados da sessão, incluindo os cookies
    if request.method == 500:
        return redirect('livros')
    else:
        
        request.session.flush()

    # Finaliza a sessão
        logout(request)
    
    
def criar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        if form.is_valid():
            
            form.save()
            # Redirecionar para a página 'livros' após o salvamento bem-sucedido
            return HttpResponseRedirect(reverse('livros'))
        else:
            return HttpResponse('DADOS INVÁLIDOS')
    
    
    

def excluir_livro(request, livro_id):
    # Verificar se a solicitação é do tipo POST
    if request.method == 'POST':
        # Tentar encontrar o livro pelo ID fornecido
        livro = get_object_or_404(Livros, id=livro_id)
        
        # Excluir o livro
        livro.delete()
        
        # Redirecionar para uma página de confirmação ou qualquer outra página desejada
        return redirect('livros')
    else:
        # Se a solicitação não for do tipo POST, redirecionar para a página inicial ou exibir uma mensagem de erro
        return redirect('livros')
    


def alugar_livro(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livros, id=livro_id)
        livro.usuario = request.user # Associa o usuário logado ao livro
        livro.emprestado = True
        livro.save()
        
        return redirect('livros')
        

def devolver_livro(request, livro_id):
    if request.method == 'POST':
        livro = get_object_or_404(Livros, id=livro_id)
        livro.usuario = None  # Remove a associação do usuário
        livro.emprestado = False  # Atualiza o status do livro para não emprestado
        livro.save()
        
        return redirect('livros')


def detalhes_livro(request, livro_id):
    # Obtém o nome do livro com o ID especificado
    if request.method == 'POST':
        livro = Livros.objects.get(id=livro_id)
        nome_livro = livro.nome

    # Prompt para a geração do texto
        prompt = f"Dê-me uma sinopse de 250 caracteres sobre o livro '{nome_livro}'."

    # Gera o texto com a OpenAI API
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250,
        n=1,
        stop="\n"
        )

    # Extrai o texto gerado da resposta
        sinopse = response.choices[0].text.strip()

    # Renderiza o template com a sinopse do livro
        return render(request, 'livros.html', {'nome_livro': nome_livro, 'sinopse': sinopse})
    

    

























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    