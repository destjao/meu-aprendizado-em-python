'''
Exercícios
Crie funcções que duplicam, triplicam e quadruplicam
o númeoro recebido como parâmetro.
'''

# number = input('Dígite um número: ')

# try:
#     number = int(number)
# except:
#     print('Você não digitu um número!')

# def duplica(num):
#     return num * 2

# def triplica(num):
#     return num * 3

# def quadruplica(num):
#     return num * 4

# print(duplica(number))
# print(triplica(number))
# print(quadruplica(number))

def multiplicador(mult):
    def multiplicar(num):
        return num * mult
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))