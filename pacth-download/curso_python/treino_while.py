'''AULAS EXTRAS DE WHILE PARA FIXAÇÃO'''

# # n_numeros = 0
# # contador = 50

# # while n_numeros < contador:
# #     n_numeros += 1
# #     print(n_numeros)

# # print('Contagem finalizada!')

'''----------------------------------------------------------------------------------------------------------------'''

# # n = 50
# # subtracao = 0

# # while n > subtracao:
# #     print(n)
# #     n -= 1

# # print('Subtração finalizada!')

# # n = 2
# # mult = 2048

# # while n < mult:
# #     n *= 2
# #     print(n)

# # print('O número foi multiplicador por 2 até atingir 2048!')

'''----------------------------------------------------------------------------------------------------------------'''

# # n = 1000
# # div = 5

# # while n >= div:
# #     print(n)
# #     n /= div
# #     if n < div:
# #         print(n)
# # print(f'O número 1000 dividido por {div} resultou em {n}, resultando a não possibilidade de mais divisões!')

'''----------------------------------------------------------------------------------------------------------------'''

# # n = 10
# # p = 0
# # q = 1

# # if p <= 10:      # SE O VALOR DE (P = 0) FOR MENOR OU IGUAL A (N = 10) CONDIÇÃO TRUE
# #     while n > p:
# #         p += 1
# #         print(p)

# # if p >= q:      # SE O VALOR DE (P = 10) FOR MAIOR QUE (Q = 0) A CONDIÇÃO TRUE
# #     while p > q:
# #         p -= 1
# #         print(p)
        
'''----------------------------------------------------------------------------------------------------------------'''

# # n = 0
# # p = 10

# # while n <= p:
# #     n += 1
# #     print(n)
# #     if n == 7:
# #         print('Odeio o número 7 para por aqui...')
# #         break
    
'''----------------------------------------------------------------------------------------------------------------'''

# # n = 0
# # p = 10

# # while n < p:
# #     n += 1

# #     if n >= 4 and n <= 7:
# #         print(f'Cadê o {n}?')
# #         continue

# #     print(n)

'''----------------------------------------------------------------------------------------------------------------'''

# # n = 1
# # p = 10

# # while n <= p:
# #     n += 1
# #     par = n % 2

# #     if par == 1:
# #             print(f'O número {n} é ímpar!')

# #     if par == 0:
# #         print('Não quero ver número par!')
# #         continue

'''----------------------------------------------------------------------------------------------------------------'''

# # linhas = 2
# # colunas = 2

# # linha = 1
# # while linha <= linhas:
# #     coluna = 1
# #     while coluna <= colunas:
# #         print(linha, coluna)
# #         coluna += 1
# #     linha += 1

'''----------------------------------------------------------------------------------------------------------------'''

# # print('Seja bem vindo a sua tábuada em python')
# # n = int(input('Dígite um número: '))
# # m = 1

# # while m <= 10:
# #     soma = n * m
# #     print(f'{n} * {m} = {soma}')
# #     m += 1

'''----------------------------------------------------------------------------------------------------------------'''

# # frase = 'Porra jamelão!'
# # i = 0
# # size = len(frase)
# # nova_frase = ''

# # while i < size:
# #     letra = frase[i]
# #     nova_frase += letra + '*'
# #     i += 1
# # print(f'*{nova_frase}')

'''----------------------------------------------------------------------------------------------------------------'''

# # while True:
    
# #     menu = input('Bem vindo ao menu, você deseja Calcular[C] ou Sair[S]: ').lower()
# #     if menu == 's':
# #         break
    
# #     elif menu == 'c':
# #         n1 = input('Dígite um número: ')
# #         n2 = input('Dígite outro número: ')
# #         oper = str(input('Dígite o operador: '))
        
# #         try:
# #             n1_float = float(n1)
# #             n2_float = float(n2)
# #         except:
# #             print('Número invalido')
# #             continue

        
# #         interlock = type(n1_float) and type(n2_float) is float
# #         interlock_oper = oper in '+-*/'
# #         # print(n1, n2, oper)
# #         # print(interlock, interlock_oper)

# #         if interlock and interlock_oper == True:

# #             if interlock == True:

# #                 if oper == '+':
# #                     soma = n1_float + n2_float
# #                     print(f'{n1} + {n2} = {soma}')

# #                 if oper == '-':
# #                     soma = n1_float - n2_float
# #                     print(f'{n1} - {n2} = {soma}')

# #                 if oper == '*':
# #                     soma = n1_float * n2_float
# #                     print(f'{n1} * {n2} = {soma}')

# #                 if oper == '/':
# #                     soma = n1_float / n2_float
# #                     print(f'{n1} / {n2} = {soma}')

# #         else:
# #             print('Operador inválido!')
# #     else:
# #         print('Não consegui entender oque quis dizer, escreva [s] para sair ou [c] para cálcular')
# #         continue