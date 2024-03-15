# Métodos em instancia de classes Python
class Carro:
    # Atributos = Nome, Marca...
    # Métodos = Acelerar, Freiar...
    def __init__(self, nome):
        self.nome = nome # Hard coded - É algo escrito diretamente

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()