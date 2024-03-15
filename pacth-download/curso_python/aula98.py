import importlib

import aula98_m # Modulo e um sigle tons

# print(aula98_m.var)
for i in range(10):
    importlib.reload(aula98_m)
    print(i,i)
    i += 1