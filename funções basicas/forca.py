import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desafio", "computador", "jogo", "algoritmo", "openai"]

# Escolha aleatória de uma palavra da lista
palavra = random.choice(palavras)

# Inicialização das variáveis
letras_corretas = []
letras_erradas = []
tentativas_restantes = 6

# Função para exibir a palavra com as letras corretas reveladas
def exibir_palavra():
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

# Laço principal do jogo
while True:
    print("\nPalavra:", end=" ")
    exibir_palavra()
    print("Letras erradas:", letras_erradas)
    print("Tentativas restantes:", tentativas_restantes)
    
    # Verificar se o jogador venceu
    if all(letra in letras_corretas for letra in palavra):
        print("\nParabéns, você venceu!")
        break
    
    # Verificar se o jogador perdeu
    if tentativas_restantes == 0:
        print("\nGame over! A palavra era:", palavra)
        break
    
    # Solicitar uma letra ao jogador
    letra = input("Digite uma letra: ").lower()
    
    # Verificar se a letra já foi tentada
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já tentou esta letra. Tente outra.")
        continue
    
    # Verificar se a letra está na palavra
    if letra in palavra:
        print("Letra correta!")
        letras_corretas.append(letra)
    else:
        print("Letra errada!")
        letras_erradas.append(letra)
        tentativas_restantes -= 1
