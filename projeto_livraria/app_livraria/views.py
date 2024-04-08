from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages  # Importe a biblioteca de mensagens do Django
from .models import Usuario

def login(request):
    if request.method == 'POST':
        email = request.POST.get('inputEmail')
        senha = request.POST.get('inputPassword')

        # Verifica se o usuário com o email e senha fornecidos existe na tabela de Usuário
        usuario = Usuario.objects.filter(email=email, senha=senha).first()

        if usuario is not None:
            # Usuário autenticado com sucesso
            # Redireciona para a página de tarefas
            return redirect('livros')
        else:
            # Credenciais inválidas
            mensagem = "Email ou senha incorretos. Por favor, tente novamente."
            messages.error(request, mensagem)  # Adicione a mensagem de erro

            # Redireciona de volta para a página de login
            return redirect('login')
    else:
        return render(request, 'cadastro/index.html')
    


def signup(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirmaSenha')

        # Validação dos campos
        if not nome:
            messages.error(request, 'O campo Nome é obrigatório.')
        if not sobrenome:
            messages.error(request, 'O campo Sobrenome é obrigatório.')
        if not email:
            messages.error(request, 'O campo Email é obrigatório.')
        if not senha:
            messages.error(request, 'O campo Senha é obrigatório.')
        if senha != confirma_senha:
            messages.error(request, 'As senhas não coincidem.')

        # Se não houver erros de validação, crie o usuário
        if not messages.get_messages(request):
    # Crie o usuário com os dados fornecidos
            nome_completo = f"{nome} {sobrenome}"
            Usuario.objects.create(
        nome=nome_completo,
        email=email,
        senha=senha
        )
            # Redirecione para algum lugar após o cadastro
        return redirect('login')

    # Se a solicitação for GET ou se houver erros de validação, renderize o template do formulário de cadastro
    return render(request, 'cadastro/signup.html')




def livros(request):
    return render(request, 'cadastro/livros.html')
