letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('Good!')
        break

    print(letras)