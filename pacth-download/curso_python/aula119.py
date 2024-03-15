# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


tarefas = ['Tomar Café', 'Caminhar', 'Ler', 'Ouvir Podcast']
tarefas_removidas = []

while True:
    flag_t = (bool(tarefas))
    flag_tr = (bool(tarefas_removidas))

    print('TAREFAS | OPÇÕES | LISTAR, DESFAZER, REFAZER')
    print()
    for tarefa in tarefas:
        print(tarefa)
    print()
    
    def fazer(tarefas, add):
        tarefas.append(add)

    def desfazer(tarefas, tarefas_removidas):
        if flag_t == False:
            return None
        tarefa = tarefas.pop()
        tarefas_removidas.append(tarefa)

    def refazer(tarefas, tarefas_removidas):
        if flag_tr == False:
            return None
        tarefa = tarefas_removidas.pop()
        tarefas.append(tarefa)


    realizar_tarefa = input('Dígite a opção que deseja: ')
    realizar_tarefa = realizar_tarefa.upper()

    if realizar_tarefa == 'LISTAR':
        tarefa = input('Dígite a tarefa: ')
        fazer(tarefas, tarefa)
    elif realizar_tarefa == 'DESFAZER':
        desfazer(tarefas, tarefas_removidas)
    elif realizar_tarefa == 'REFAZER':
        refazer(tarefas, tarefas_removidas)
    elif realizar_tarefa == 'CLEAR':
        os.system('cls')
    else:
        print('Opção Inválida!')
    

