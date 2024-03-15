class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_clase(cls):
        print('Hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
p1 = Pessoa('Joao', 34)
print(Pessoa.ano)
p1.metodo_de_clase()