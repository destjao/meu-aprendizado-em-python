# # Exercícios com funções

# # Crie uma função que multiplica todos os argumentos
# # não nomeados recebidos
# # Retorne o total para uma variável e mostre o valor
# # da variável.

# def mult (*args):
#     acc = 1
#     for n in args:
#         acc *= n
#     return acc

# multiplica = mult(1,2,3,4,5)
# print(multiplica)

# '''------------------------------'''
import random

# def par_impar(numero):
#     return numero % 2 == 0

# print(par_impar(2))
# print(par_impar(3))

# def random_number(num):
#     return num % 2 == 0

# for n in range(1,30):
#     rn = random.randint(0, 10000)
#     if random_number(rn) == True:
#         print(f'O núemro {rn} é par!')
#     else:
#         print(f'O número {rn} é ímpar!')

# import time
# n = 0
# n2 = 0
# n3 = 0
# n4 = 0
# data = ''
# alfabeto = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

# while True:
#     for letra in alfabeto:
#         n1 = random.randint(0,9)
#         n2 = random.randint(0,9)
#         n3 = random.randint(0,9)
#         n4 = random.randint(0,9)
#         data += letra
#         data += str(n1)
#         data += str(n2)
#         data += str(n3)
#         data += str(n4)
#         print(data)
#         time.sleep(1)
#         data = ''
    
    # if time.sleep(15):
    #     continue
    # print(data)
    
# numeros = list(range(10))  # Cria uma lista de números de 0 a 9
# letras = list('abcdefghijklmnopqrstuvwxyz')  # Cria uma lista de letras de 'a' a 'j'

# i = 0
# while i < len(numeros):
#     for j in range(len(letras)):
#         if i == j:
#             numeros.insert(i, letras[j])
#             break
#     print(''.join(str(e) for e in numeros))
#     numeros = list(range(10))  # Reset a lista de números para a próxima iteração
#     i += 1

# import itertools
# import time

# # Definindo os caracteres que serão usados
# numeros = '0123456789'
# letras = 'abcdefghij'

# # Criando todas as combinações possíveis
# combinacoes = list(itertools.product(numeros, repeat=10)) + list(itertools.product(letras, repeat=10))

# # Imprimindo as combinações
# for combinacao in combinacoes:
#     print(''.join(combinacao))
#     time.sleep(1)

# import itertools
# import random

# # Definindo os caracteres que serão usados
# numeros = '0123456789'
# letras = 'abcdefghij'

# # Criando todas as combinações possíveis
# combinacoes = list(itertools.product(numeros + letras, repeat=10))

# # Selecionando 100 combinações aleatórias
# combinacoes_selecionadas = random.sample(combinacoes, 100)

# # Imprimindo as combinações selecionadas
# for combinacao in combinacoes_selecionadas:
#     print(''.join(combinacao))

import random
import string

numeros = '0123456789'
letras = string.ascii_letters 

conta = 0
combinacoes_passadas = set()

while True:
    combinacao = ''.join(random.choice(numeros + letras) for _ in range(10))
    if combinacao in combinacoes_passadas:
        continue
    combinacoes_passadas.add(combinacao)
    print(combinacao)
    conta += 1
    if 's66' in combinacao:
        print(f'{conta}')
        break
