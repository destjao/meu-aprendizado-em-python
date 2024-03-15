# Atributos que começam com 1 ou 2 _ UnderLine não 
# devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self.cor_tampa = None

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU AQUI')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

      
pen = Caneta('Azul')
pen.cor = 'Vermelha'
pen.cor_tampa = 'Preta'
print(pen.cor_tampa, pen.cor)
# getter -> obter valor
# print(pen.cor)