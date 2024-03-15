# class Pessoa:
#     def __init__(self):  # Adicione os argumentos aqui
#         self._nome = None
#         self._idade = None
#         self._altura = None
#         self._peso = None

#     @property
#     def pessoa(self):
#         return self._nome, self._idade, self._altura, self._peso
    
#     @pessoa.setter
#     def pessoa(self, value):  # value deve ser uma tupla contendo (name, i, a, p)
#         self._nome, self._idade, self._altura, self._peso = value

# alguem = Pessoa()  # Agora os argumentos são aceitos

# alguem.pessoa = 'João', '22', '1.83m', '90kg'

# print(alguem.pessoa)

# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class Foo:
    def __init__(self):
        self.public = 'Isso aqui é publico!'
        self._protect = 'Isso aqui é protegido'
        self.__private = 'Isso aqui é privado'

    def meth_public(self):
        print(self.__private)
        return 'Meth Public'

    def _meth_protect(self):
        return 'Meth Protect'
    
    def __meth_private(self):
        return('Meth Private')

f = Foo()
# print(f.public)
# print(f._protect)
# print(f._meth_protect())
print(f.meth_public())
print(f._Foo__meth_private())