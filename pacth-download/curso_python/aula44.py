'''
For + range
range -> range(start, stop, step)
start = início do range
stop = fim do range
step = define o formato da contagem 
step(1) exemplo: conta de uma em uma casa.'''

# numbers = range(1, 11)

# for number in numbers:
#     print(number)

n = range(2, 100, 2)

print('Esses são os multíplos de 2')
for i in n:
    print(f'{i=}')