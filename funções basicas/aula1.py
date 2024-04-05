

#nome = input('Qual o seu nome? ')
#altura = float(input('Sua altura (em metros)? '))
#peso = float(input('Seu peso (em quilos)? '))

#MC = peso / (altura ** 2)

#print(f'{nome}, tem {altura}, metros de altura, pesa, {peso}, quilos e seu IMC é, {IMC}')

while True:
    try:
        num1 = int(input('Digite um valor: '))
        break  
    except ValueError:
        print('Favor digitar um número válido.')

while True:
    try:
        num2 = int(input('Digite outro valor: '))
        break  
    except ValueError:
        print('Favor digitar um número válido.')
        
if num1 > num1 :
    print('Valor 1 é maior que o valor')
    
elif num1 == num2:
    print('os valores são iguais')
    
else:
    print('Valor 2 é maior que valor 1')