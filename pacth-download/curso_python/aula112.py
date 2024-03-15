# filter é um filtro funcional
def print_inter(iter):
    print(*list(iter), sep='\n')
    print()

produtos = [
    {'nome': 'p5', 'preco': 10.00},
    {'nome': 'p1', 'preco': 22.36},
    {'nome': 'p3', 'preco': 10.11},
    {'nome': 'p2', 'preco': 105.87},
    {'nome': 'p4', 'preco': 69.90},
]

# novos_produtos = [
#     p for p in produtos if p['preco'] < 90
# ]

novos_produtos = filter(
    lambda p: p['preco'] > 100,
    produtos
)

print_inter(produtos)
print_inter(novos_produtos)