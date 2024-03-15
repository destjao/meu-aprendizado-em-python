"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# input_number = input('Dígite um número: ')
# if input_number.isdigit(): # Use .isdigit para verificar se e um número
#     number = int(input_number)
#     if type(number) is int: # Use type() para verificar a classe
#         if number % 2 == 0:
#             print(number % 2)
#             print(f'O número {number} é par!')
#         else:
#             print(number % 2)
#             print(f'O número {number} é ímpar!')
#     else:
#         print('Você não digitou um número inteiro!')
# else:
#     print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# data = int(input('Dígite a hora: '))
# name = input('Dígite seu nome: ')

# dia = data <= 11
# tarde = data >= 12 and data <=17
# noite = data >=18 and data <=23

# if dia:
#     print(f'Olá senhor {name}, bom dia!')
# elif tarde:
#     print(f'Olá senhor {name}, boa tarde!')
# elif noite:
#     print(f'Olá senhor {name}, boa noite!')
# else:
#     print(f'Olá senhor {name}, você dígitou uma hora que não e válida!')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Qual o seu nome: ')
name_size = len(name)
short_name = name_size <= 4 and name_size > 0
medium_name = name_size >=5 and name_size <=6
big_name = name_size > 6
none_name = not name
print(none_name)

if none_name:
    print('Você não dígitou nada!')
else:
    if short_name:
        print(f'Olá senhor {name} seu nome é curto!')
    elif medium_name:
        print(f'Olá senhor {name} seu nome é médio!')
    else:
        print(f'Olá senhor {name} seu nome é grande!')