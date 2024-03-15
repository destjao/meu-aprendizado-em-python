'''Argumentos nomeados e não nomeados
    Refatorar : editar o seu código
'''

def soma(x, y, z=None):
    if z is None:
        print(x + y)
    else:
        print(x + y + z)
soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(1,23,4)