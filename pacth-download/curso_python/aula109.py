# Combinations, Permutations e Product - Itertools
from itertools import combinations, permutations, product

def print_iter(iter):
    print(*list(iter), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino'],
]

# print_iter(combinations(pessoas, 3))
# print_iter(permutations(pessoas, 3))
print_iter(product(*camisetas))

