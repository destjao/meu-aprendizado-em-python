name = input('Qual é o seu nome: ')
age =  input('Qual a sua idade: ')

if name and age:
    name_inverso = name[::-1]
    name_number_words = len(name)
    first_word_name = name[0]
    calculate_last_word_name = name_number_words - 1
    last_word_name = name[calculate_last_word_name]
    no_space_name = name
    
    print('Seu nome é {}'.format(name))
    print('Seu nome ao contrario é {}'.format(name_inverso))
    if ' ' in name:
        print('Seu nome comtém espaços')
    else:
        print('Seu nome não contém espaços')
    print('Seu nome tem {} letras'.format(name_number_words))
    print('A primeira letra do seu nome é {}'.format(first_word_name))
    print('A última letra do seu nome é {}'.format(last_word_name))
else:
    print('Você não cumpriu os requisitos de cadastro!')