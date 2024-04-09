from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages  # Importe a biblioteca de mensagens do Django
from .models import Usuario
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def livros(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        senha = request.POST.get('inputPassword')
        
        # Verifica se o usuário com o email e senha fornecidos existe na tabela de Usuário
        usuario = Usuario.objects.filter(email=email, senha=senha).first()

        if usuario is not None:
            # Usuário autenticado com sucesso
            return render(request, 'cadastro/livros.html', {'usuario': usuario})
        else:
            # Credenciais inválidas
            messages.error(request, "Email ou senha incorretos. Por favor, tente novamente.")
            return redirect('login')  # Redireciona de volta para a página de login

    # Se não for uma requisição POST, renderiza o template de login
    return redirect('login')  # Redireciona de volta para a página de login se o usuário tentar acessar diretamente a URL


    



def signup(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmaSenha')

        # Lista para armazenar mensagens de erro
        erros = []

        # Validação dos campos
        if not nome:
            erros.append('O campo Nome é obrigatório.')
        if not sobrenome:
            erros.append('O campo Sobrenome é obrigatório.')
        if not email:
            erros.append('O campo Email é obrigatório.')
        if not senha:
            erros.append('O campo Senha é obrigatório.')
        if senha != confirma_senha:
            erros.append('As senhas não coincidem.')

        # Se houver erros, exibe as mensagens de erro
        if erros:
            for erro in erros:
                messages.error(request, erro)
        else:
            
            # Cria o usuário com os dados fornecidos
            nome_completo = f"{nome} {sobrenome}"
            Usuario.objects.create(nome=nome_completo, email=email, senha=senha)

            # Redireciona para a página de login após o cadastro
            return render(request, 'cadastro/signup.html', {'cadastrado': True})

    # Renderiza o template do formulário de cadastro
    return render(request, 'cadastro/signup.html')




def finalizar_sessao(request):
    logout(request)
    return redirect('login')

def livros(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        senha = request.POST.get('inputPassword')
        
        # Verifica se o usuário com o email e senha fornecidos existe na tabela de Usuário
        usuario = Usuario.objects.filter(email=email, senha=senha).first()

        if usuario is not None:
            # Usuário autenticado com sucesso
            return render(request, 'cadastro/livros.html', {'usuario': usuario})
        else:
            # Credenciais inválidas
            messages.error(request, "Email ou senha incorretos. Por favor, tente novamente.")
            return redirect('login')  # Redireciona de volta para a página de login

    # Se não for uma requisição POST, renderiza o template de login
    return redirect('livros')  # Redireciona de volta para a página de login se o usuário tentar acessar diretamente a URL