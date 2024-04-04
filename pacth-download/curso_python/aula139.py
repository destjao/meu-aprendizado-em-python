# class MinhaString(str):
#     def upper(self):
#         print('Chamou UPPER'.upper())
#         return super().upper()
#     ...
    
# str = MinhaString('João')
# print(str.upper())

class A:
    atribut_a = 'valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo
    
    def method(self):
        print('A')

class B(A):
    atribut_b = 'valor b'
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def method(self):
        print('B')
        
class C(B):
    atribut_c = 'valor c'
    def method(self):
        print('C')
        

# print(C.mro())      
c = C('Atributo Mermão', 'Outra coisa')
print(c.atributo)
print(c.outra_coisa)
print(c.atribut_a)
print(c.atribut_b)
print(c.atribut_c)
c.method()