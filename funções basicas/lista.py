
lista_numeros = [1, 2, 3]

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

lista_vazia = []

lista_vazia.append("olá")

lista_vazia.append("mundo")

print(lista_vazia)

numeros = [10,9,8,7,6]

print('total de numeros: ', len(numeros))
print('maior numero: ', max(numeros))
print('menor numero: ', min(numeros))



#LISTA PARA CRIAR NOTAS E LISTAR ELES
notas = []

for x in range(5):
    codigo_aluno = input("RM: ")
    notaa = float(input("Nota: "))
    resultado = [codigo_aluno, notaa]
    notas.append(resultado)
    
print( "quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM ", codigo_aluno, "tirou a nota:", nota)