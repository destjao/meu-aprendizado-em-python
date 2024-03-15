class Animal:

    def __init__(self, nome) -> None:
        self.nome = nome

        var = 'valor'
        print(var)
        
    def comendo(self, food):
        return f'{self.nome} está comendo {food}'
    
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('maça'))