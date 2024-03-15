# Atributos de classes
class Person:
    attribute = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_born_year(self):
        return (self.attribute - self.age)
    
p1 = Person('João', 22)
p2 = Person('Helena', 12)
print(p1.get_born_year())
print(p2.get_born_year())
