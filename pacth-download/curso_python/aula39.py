name = 'João Vitor'

size_name = len(name)

indice = 0
new_name = ''
while indice < len(name):
    letra = name[indice]
    new_name += f'*{letra}'
    indice += 1
new_name += '*'
print(new_name)