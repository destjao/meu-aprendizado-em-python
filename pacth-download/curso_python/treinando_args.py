# def somando_numero(**kwargs):
#     return kwargs

# # Chamando a função com argumentos nomeados corretamente
# resultado = somando_numero(nome="João", idade=19)

# # Imprimindo o resultado
# print(resultado)
def soma(**kwargs):
    return sum(kwargs)

res = soma(2, 1)