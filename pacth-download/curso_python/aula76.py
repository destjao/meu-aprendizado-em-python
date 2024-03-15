# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# print()

# for key in pessoa:
#     print(key, pessoa[key])

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'João Vitor'


# print(pessoa)
# print(pessoa['nome'])

# if pessoa.get('sobrenome'):
#     print('EXISTE')

'''
Métodos úteis dos dicionários em Python
len = Quantas chaves
keys = Interável com chaves
values = Interável com valores
items = Interável com chaves e valores
setdefault = Adicionar valor se a chave não existir
copy = Retorna uma cópia rasa
get = Obtém uma chave
pop = Apaga um item com a chave especificada (del)
popitem = Apaga o útimo item adicionado
uptade = Atualiza um dicionário com outro
'''
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))

# for chave in pessoa.values():
#     print(chave)

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
p1.update(nome='novo valor', idade=26)
print(p1)