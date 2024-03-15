# reduce - faz a redução de um iterável em um valor
from functools import reduce
produtos = [
    {'nome': 'p5', 'preco': 10},
    {'nome': 'p1', 'preco': 22},
    {'nome': 'p3', 'preco': 2},
    {'nome': 'p2', 'preco': 6},
    {'nome': 'p4', 'preco': 4},
]

def funcao(acc, produto):
    print('Acumulador', acc)
    print('Produto', produto)
    print()
    return acc + produto['preco']

total = reduce(
    funcao,
    produtos,
    0
)

print(f'TOTAL: {total}')


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)