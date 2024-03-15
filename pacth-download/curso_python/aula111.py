from functools import partial

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()

produtos = [
    {'nome': 'p5', 'preco': 10.00},
    {'nome': 'p1', 'preco': 22.36},
    {'nome': 'p3', 'preco': 10.11},
    {'nome': 'p2', 'preco': 105.87},
    {'nome': 'p4', 'preco': 69.90},
]

def aumentar(valor, percent):
    return round(valor*percent,2)

aumentar_dez_percent = partial(
    aumentar, percent=1.1
)

# novos_produtos = [

#     {**p, 'preco': aumentar_dez_percent(p['preco'])} for p in produtos
# ]

def muda_price(produto):
    return {**produto, 'preco': aumentar_dez_percent(produto['preco'])}

novos_produtos = map(
    muda_price, produtos
)


print_iter(produtos)
print_iter(novos_produtos)

print(list(map(
        lambda x: x * 3,
          [1,2,3,4]
          )
          )
)