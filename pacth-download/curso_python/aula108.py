# count é um interador sem fim
from itertools import count

c1 = count(1)
r1 = range(10)

for i in c1:
    if i > 10:
        break
    print(i)