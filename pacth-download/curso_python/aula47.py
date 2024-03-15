"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume' # A palavra deve está fora do while para não ser resetada
letras_acertadas = '' # Do lado de fora para não perder as letras acertadas
n_tentativas = 0 # Quantidades de tentativas até acertar a palavra

while True: # Cria um loop infinito

    letra_digitada = input('Dígite uma letra: ') # Coleta uma letra
    n_tentativas += 1

    if len(letra_digitada) > 1: # Verifica se foi realmente dígitado apenas uma letra
        print('Dígite apenas uma letra.')
        continue # Caso dígitada mais que uma letrar retorna novamente a solicitação
    
    if letra_digitada in palavra_secreta: # Verifica se a letra digitada está na palavra secreta
        letras_acertadas += letra_digitada # Se a letra digitada estiver na palavra secreta, adiciona a letra a váriavel letras acertadas

    palavra_formada = '' # Variavél de mémoria da palavra sendo formada

    for letra_secreta in palavra_secreta: # Aqui cria um loop para verificar se a letra digitada está entre a palavra ou não
        if letra_secreta in letras_acertadas: # Caso a letra digitada esteja entre a palavra a letra e salva e exibida
            palavra_formada += letra_secreta # Concatena letra acertada a variavél de palavra formada
        else: # Caso a letra não esteja se mantém escondida por *
            palavra_formada += '*' # Concatena * em palavra formada caso não houver acerto

    print(palavra_formada)

    if palavra_formada == palavra_secreta:

        os.system('cls') # Código para limpar o terminal
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Número de tentativas {n_tentativas}')

        letras_acertadas = '' # Do lado de fora para não perder as letras acertadas
        n_tentativas = 0 # Quantidades de tentativas até acertar a palavra
    
