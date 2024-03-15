'''Calculadora com while'''
while True:
    number_1 = input('Dígite um número: ')
    number_2 = input('Dígite um número: ')
    operador = input('Dígite um operador (+-/*): ')

    number_validos = None
    
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        number_validos = True
    except:
        number_validos = None

    if number_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operador_valido = '+-/*'

    if operador not in operador_valido:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Dígite apenas um operador.')
        continue
    print('Realizando o cálculo...')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    if operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)

    sair = input('Dígite [s] para sair: ').lower().startswith('s')
    print(sair)
    
    if sair is True:
        break