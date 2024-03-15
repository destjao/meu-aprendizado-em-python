"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = ['Arroz', 'Feijão', 'Macarrão']
precos = [23.99, 11.50, 2.35]

while True:
    
    os.system('cls')

    print('1 - Adicionar item')
    print('2 - Deletar item')
    print('3 - Ver lista')
    print('0 - Sair')

    opcao = input('Digite a opção desejada: ')

    while opcao == '1' or '2' or '3':

        if opcao == '1':
            print('----QUAL ITEM DESEJA ADICIONAR----')
            n = 0
            for a, b in enumerate(lista):
                n += 1
                print(n, b, f'{precos[a]}R$')
            lista.append(input('Item: '))
            precos_input = input('Preço: ').replace(',', '.')
            validador = None
        
            try:
                precos_valid = float(precos_input)
                precos.append(precos_valid)
                validador = True
            except:
                validador = None

                if validador == None:
                    lista.pop()
                    print('Você não adicionou o preço do seu produto, tente novamente.')

            prosseguir = input('Enter para continuar | [s]air: ').lower()
            if prosseguir == 's':
                break
            elif prosseguir != '':
                print('Opção inválida')
                break

        elif opcao == '2':
            print('----QUAL ITEM DESEJA DELETAR----')
            
            if len(lista) > 0:
                for a, b in enumerate(lista, start=1):
                    print(a, b)

                delete = input('Dígite o número do item que deseja apagar: ')
                validador = None

                try:
                    delete_int = int(delete)
                    delete_int -= 1
                    validador = True

                except:
                    validador = None
                    if validador == None:
                        print('Você não dígitou um número válido!')
                        continue

                if delete_int < len(lista):
                    lista.pop(delete_int)
                    precos.pop(delete_int)
                else:
                    print('Não achei o item que deseja apagar!')
                    continue

                break  
            else:
                print('Sua lista está vazia')
                input('Pressione enter para sair...')
                break

        elif opcao == '3':
            print('----ESSA E A SUA LISTA----')
            if len(lista) == 0:
                print('Sua lista está vazia')
                input('Pressione enter para sair...')
                break
            else:
                n = 0
                for a, b in enumerate(lista):
                    n += 1
                    print(n, b, f'{precos[a]}R$')
                input('Pressione enter para sair...')
                break

        else:
            print('Opção inválida. Tente novamente.')
            break

    if opcao == '0':
            print('Saindo do programa.')
            break