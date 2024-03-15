# string  = 'Luiz'
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('João', 'Vitor')
# p1.nome = 'João'
# p1.sobrenome = 'Vitor'
print(p1.nome, p1.sobrenome)