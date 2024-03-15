'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e x - Hexadecimal (ABCDEF0123456789)
'''
nome = 'João'
nome1 = 'Gabriel'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f, oque achou %s' % (nome, preco,nome1)
print(variavel)
print('O hexadecimal de %d é %08x' % (15, 15))