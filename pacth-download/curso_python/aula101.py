# Exercício - Adiando execuções de funções

def soma(x, y):
    return x + y

def mult(x, y):
    return x * y

def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_5 = executa(soma, 5)
multiplica_com_10 = executa(mult, 10)
