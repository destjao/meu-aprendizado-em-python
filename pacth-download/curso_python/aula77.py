'''Exercícios - sistema de perguntas e respostas'''

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# for i in enumerate(perguntas):
#     print()

# while True:
#     question1 = perguntas[0]
#     question2 = perguntas[1]
#     question3 = perguntas[2]

#     opção1 = question1['Opções']
#     opção2 = question2['Opções']
#     opção3 = question3['Opções']

#     # escolha = 'abcd'

#     print(question1['Pergunta'])
#     for i in enumerate(opção1):
#         print(i[0],')', i[1])
    
#     resposta1 = 2
#     resposta = input('Qual a resposta correta: ')

#     try:
#         resposta = int(resposta)
#     except:
#         ('Você não dígitou uma opção válida!')

#     if resposta == 2:
#         print('Você acertou a resposta correta é', opção1[2],'!!')
#     else:
#         print('Você errou!')
#     break

for pergunta in perguntas:
    print(pergunta['Pergunta'])