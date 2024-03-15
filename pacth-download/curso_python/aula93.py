# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try: # tenta (Não e uma boa prática!)
    a = 18
    b = 0
    c = a / b
    
except ZeroDivisionError as error:
    print('Não deu amigo!', error)

except NameError:
    print('Não deu amigo!')

except (TypeError, IndexError) as error:
    print('Não deu amigo!', error)

except Exception:
    print('Não deu amigo!')

