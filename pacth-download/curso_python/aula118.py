# Problemas dos parâmetros mutáveis em funções
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('João')
adiciona_clientes('Luiz', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Jorge')
adiciona_clientes('Pedro', cliente2)
print(cliente2)