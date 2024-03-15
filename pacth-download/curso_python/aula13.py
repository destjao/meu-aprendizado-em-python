name = str(input('Seu nome: '))
height = float(input('Sua altura: '))
weight = float(input('Seu peso: '))

imc = weight / (height**2)

print(f'Olá senhor {name}, você tem {height}m de altura, pesa {weight}kg e seu IMC atual é de {imc:.2f}')