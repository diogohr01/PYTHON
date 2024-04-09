from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages  # Importe a biblioteca de mensagens do Django
from .models import Usuario
from django.contrib.auth import logout


def login(request):
    erros = []  # Inicializa a lista de erros

    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        senha = request.POST.get('inputPassword')
        
        if not email:
            erros.append('Preencha o Email.')
        if not senha:
            erros.append('Preencha a senha.')

        if erros:
            # Se houver erros, exibe as mensagens de erro
            for erro in erros:
                messages.error(request, erro)
            
        
        # Verifica se o usuário com o email e senha fornecidos existe na tabela de Usuário
        usuario = Usuario.objects.filter(email=email, senha=senha).first()

        if usuario is not None:
            # Usuário autenticado com sucesso
            # Redireciona para a página de tarefas
            return render(request, 'index.html', {'logado': True})
        else:
            # Credenciais inválidas
            erros.append("Email ou senha incorretos. Por favor, tente novamente.")
            # Adicione a mensagem de erro

            # Redireciona de volta para a página de login
            return redirect('login')

    # Se não for uma requisição POST, renderiza o template de login
    return render(request, 'index.html')


    



def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html')

    else:    # Obtém os dados do formulário
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
            return render(request, 'signup.html', {'cadastrado': True})

    # Renderiza o template do formulário de cadastro




def livros(request):
    

    return render(request, 'cadastro/livros.html')

def finalizar_sessao(request):
    logout(request)
    return redirect('login')