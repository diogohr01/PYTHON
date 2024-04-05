def parse_numero(numero):
    if ',' in numero:
        return float(numero.replace(',', '.'))
    elif '.' in numero:
        return float(numero)
    else:
        try:
            return int(numero)
        except ValueError:
            return None

while True:
    # Input do usuário
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite um operador (+ - * /): ')

    # Checando se o número é válido
    n1_float = parse_numero(numero1)
    n2_float = parse_numero(numero2)

    if n1_float is None or n2_float is None:
        print('Por favor, digite um número válido')
        continue

    # Checando se o operador é válido
    operadores_validos = '+-*/'
    if len(operador) != 1 or operador not in operadores_validos:
        print('Por favor, digite um operador válido')
        continue

    # Realizando a operação
    if operador == '+':
        resultado = n1_float + n2_float
    elif operador == '-':
        resultado = n1_float - n2_float
    elif operador == '*':
        resultado = n1_float * n2_float
    elif operador == '/':
        if n2_float == 0:
            print('Não é possível dividir por zero')
            continue
        resultado = n1_float / n2_float
        

    print(f'O resultado da operação é: {resultado}')

    # Sair da calculadora
    sair = input('Deseja sair da calculadora? (sim/não): ').lower()
    if sair.startswith('s'):
        break
