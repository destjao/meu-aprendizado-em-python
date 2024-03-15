frase = 'O Python é uma linguagem de programação.' \
        'multiparadigma. ' \
        'Python foi criado por Guido Van Rossum.'

i = 0
amv = 0
lqamv = ''
while i < len(frase):
    letra_atual = frase[i]
    qvla = frase.count(letra_atual)


    if letra_atual == ' ':
        i += 1
        continue

    if amv < qvla:
        amv = qvla
        lqamv = letra_atual

    print(letra_atual, qvla)
    i += 1

print('A letra que apareceu mais vezes foi' f'{lqamv} que apareceu ' f'{amv}x')