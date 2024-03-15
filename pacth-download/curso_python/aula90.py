import sys
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista)) # A lista já e salva na mémoria instantaneamente
print(sys.getsizeof(generator)) # O generator e acessado um por vez para continuar deve usar next

# for n in generator:
#     print(n)
