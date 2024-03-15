# __dict__ e vars para atributos de instância
# class Person:
#     attribute = 2023

#     def __init__(self, name, age, adress, number, city, tel):
#         self.name = name
#         self.age = age
#         self.adress = adress
#         self.number = number
#         self.city = city
#         self.tel = tel

#     def get_born_year(self):
#         return (self.attribute - self.age)
    
# dados =  {'name': 'João', 'age': 22, 'adress': 'Rua Visconde do Rio das Velhas', 'number': 206, 'city': 'Matozinhos', 'tel': '(031)97103-3656'}
# p1 = Person(**dados)

# print(p1.__dict__)

# for k, v in p1.__dict__.items():
#     print(v)

# print(p1.__dict__)
# print(vars(p1))
# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.tel)

import datetime

class Person:
    current_year = datetime.datetime.now().year

    def __init__(self, name, age, address, number, city, tel):
        self.name = name
        self.age = age
        self.address = address
        self.number = number
        self.city = city
        self.tel = tel

    def get_born_year(self):
        return (self.current_year - self.age)

    def __str__(self):
        return f'Nome: {self.name}, Idade: {self.age}, Endereço: {self.address}, Número: {self.number}, Cidade: {self.city}, Telefone: {self.tel}'

dados =  {'name': 'João', 'age': 22, 'address': 'Rua Visconde do Rio das Velhas', 'number': 206, 'city': 'Matozinhos', 'tel': '(031)97103-3656'}
p1 = Person(**dados)

print(p1)
