# raise -> lançando execeções (erros)
# def division(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError: # Aqui eu assumi o erro!
#         return d, 'ISSO E FRUTO DE UM ERRO!'

# print(division(8,0))

def erro_div_zero(d):
    if d == 0:
            raise ZeroDivisionError('Você está errado!')

def division(n, d):
        erro_div_zero(d)
        return n / d

print(division(8,0))
