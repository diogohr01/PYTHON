import os

mensagens = []

nome = input("Nome: ")

# Função para limpar a tela de acordo com o sistema operacional
def limpar_tela():
    if os.name == 'posix':
        os.system('clear')  # Para sistemas Unix (Linux, macOS)
    elif os.name == 'nt':
        os.system('cls')  # Para sistemas Windows

while True:
    limpar_tela()
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
            
    print("________")
    
    texto = input('Mensagem: ')
    if texto.lower() == "fim":
        break
    
    mensagens.append({
        "nome": nome,
        "texto": texto
    })