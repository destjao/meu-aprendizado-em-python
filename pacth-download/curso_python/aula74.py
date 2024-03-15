'''
Closure e funções que retoram outras funções
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa tarde')
s3 = criar_saudacao('Boa noite')

print(s1('João'))
print(s2('João'))
print(s3('João'))