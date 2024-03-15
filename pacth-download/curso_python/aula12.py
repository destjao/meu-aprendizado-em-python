name = str(input('Seu nome: '))
height = float(input('Sua altura: '))
weight = float(input('Seu peso: '))

imc = weight / (height**2)

print('Olá senhor {}, você tem {}m de altura, pesa {}kg e seu IMC atual é de {}'.format(name, height, weight, imc))