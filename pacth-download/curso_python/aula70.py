import random

x = 0
y = 0
z = 0

num_ran = []

for n in range(0, 30):
    def soma (x,y,z):
        return (x * y) % z
    x += random.randint(0, 100)
    y += random.randint(0, 100)
    z += random.randint(1, 100)
    print(soma(x, y, z))
    num_ran.append(str(soma(x, y, z)))
    # print(num_ran)
    x = 0
    y = 0
    z = 0

print(num_ran)







