def parametros_decorador(nome):
    def decorar(func):
        print('Decorador:', nome)

        def sua_nova_funca(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funca
    return decorar

@parametros_decorador(nome='primeiro')
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10,5)
print(dez_mais_cinco)