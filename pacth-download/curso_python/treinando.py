# lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# lista = set(lista)
# lista = list(lista)

# print(lista)

# l1 = [1,2,3]
# l2 = [3,4,5]

# l = l1 + l2

# print(set(l))

# l1 = [1,2,3,4]
# l2 = [3,4,5,6]

# ls1 = set(l1) # Transformando em um conjunto
# ls2 = set(l2)

# l = ls1 - ls2 # Realizando o cálculo para ver a diferença entre conjuntos

# print(l)

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [3,4,5,6,7,9,10]

# ls1 = set(l1)
# ls2 = set(l2)

# l = ls2.issubset(ls1)

# print(l)

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f'A chave é {chave} e o valor é {valor}')

# minha_funcao(nome= 'João', idade= 25)
# minha_funcao(nome= 'Lucas', idade= 18)

# def saudacao(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'Olá {valor}! Você e um ótimo(a) {valor}!')

# def saudacao(**kwargs):
#     for chave, valor in kwargs.items():
#         if chave == 'nome':
#             print(f'Olá, {valor}!')
#         elif chave == 'profissao':
#             print(f'Você é um ótimo {valor}!')

# saudacao(nome= 'João', profissao= 'Engenheiro')
# input('')
# saudacao(nome= 'Ana Luiza', profissao= 'Médica')
# input('')
# saudacao(nome= 'Gabriel', profissao= 'Pedreiro')
        
# def usuario(**kwargs):
#     for chave, valor in kwargs.items():
#         if chave == 'nome':
#             print(f'Olá {valor}, confirme os dados a seguir:')
#         elif chave == 'age':
#             print(f'Você tem {valor} anos?')
#         else:    
#             print(f'Seu e-mail: {valor}')

# usuario(nome='João Vitor', age=22, email='joaovitor@hotmail.com')
        

# def nome(**kwargs):
#     for chave, valor in kwargs.items():
#         print(chave, valor)

# nome(persona='João Vitor')
        

# Métodos em instancia de classes Python
        
# import random

# class Carro:
#     # Atributos = Nome, Marca...
#     # Métodos = Acelerar, Freiar...
#     def __init__(self, nome):
#         self.nome = nome # Hard coded - É algo escrito diretamente

#     def acelerar(self, velocidade):
#         print(f'{self.nome} está acelerando...')
#         print(f'O carro está há {velocidade} km/h')
#         return velocidade
    
# fox = Carro('Fox')
# velocidade_fox = fox.acelerar(velocidade=random.randint(10,100))

# if velocidade_fox > 60:
#     print(f'Você passou a {velocidade_fox} km/h')
#     print('Você foi multado, a velocidade da via e de 60km/h')
# else:
#     print(f'Você passou a {velocidade_fox} km/h')





# class Teste:
#     def __init__(self, modelo, ano):
#         self.modelo = modelo
#         self.ano = ano

#     def idade_do_carro(self, ano):
#         return 2023 - ano
    
# p1 = Teste('Chevete', 1950)

# p = p1.idade_do_carro(p1.ano)
# print(p)
        
# numbers = ['a', 'b', 'c', 'd', 'e']
# print(sum(numbers))

# def bigger_than_3(x):
#     return x > 3

# numbers = [1, 2, 3, 4, 5]
# filtered_numbers = list(filter(bigger_than_3, numbers))

# print(filtered_numbers)

# def double(x):
#     return x * 2

# mapped_items = list(map(double, numbers))

# print(mapped_items)

# from functools import reduce

# def add(x, y):
#     return x + y

# total_sum = reduce(add, numbers)

# print(total_sum)


# import json

# CAMINHO_ARQUIVO = 'tags_clp.json'

# # Carregue o arquivo JSON em uma lista de dicionários
# with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
#     db = json.load(arquivo)

# # Extraia os nomes das tags
# tag_names = [d['tag_name'] for d in db]

# # Ordene os nomes das tags em ordem alfabética
# tag_names.sort()

# # Imprima os nomes das tags
# for tag_name in tag_names:
#     print(tag_name)

# import pyautogui
# import time

# while True:
#     # Espera 5 segundos para você colocar o mouse na posição desejada
#     time.sleep(300)

#     # Obtém a posição atual do mouse
#     x, y = pyautogui.position()
#     print(x, y)
#     # Faz o clique na posição obtida
#     pyautogui.click(x, y)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time

# # Caminho para o OperaDriver
# opera_driver_path = 'C:/Users/joaov/OneDrive/Área de Trabalho/opera.exe'  # Substitua pelo caminho correto

# # URL do WhatsApp Web
# url = 'https://web.whatsapp.com/'

# # Número de telefone ou nome do contato
# contato = 'Arnon Oliveira'

# # Mensagem que você deseja enviar
# mensagem = 'Eu sinceramente fico abismado como o Arnon e gay IA, mas ele acredita fielmente que não é, ele e aquele gordalhão do Nathan!!'

# # Inicializar o driver do Opera
# options = webdriver.ChromeOptions()
# options.binary_location = opera_driver_path
# driver = webdriver.Chrome(options=options)

# # Abrir o WhatsApp Web
# driver.get(url)
# time.sleep(20)  # Aguarde o usuário fazer o login manualmente

# # Aguardar um momento para garantir que a página seja carregada
# time.sleep(5)

# # Localizar o campo de pesquisa e enviar o nome do contato
# try:
#     campo_pesquisa = driver.find_element('css selector', 'div[contenteditable="true"]')
#     campo_pesquisa.click()
#     campo_pesquisa.send_keys(contato)
#     campo_pesquisa.send_keys(Keys.ENTER)

#     # Aguardar um momento para garantir que a conversa seja carregada
#     time.sleep(5)

#     # Localizar a caixa de mensagem e enviar a mensagem
#     caixa_mensagem = driver.find_element('css selector', 'div._3Uu1_')
#     caixa_mensagem.click()
#     caixa_mensagem.send_keys(mensagem)
#     caixa_mensagem.send_keys(Keys.ENTER)
#     time.sleep(5)

# except NoSuchElementException:
#     print("Elemento não encontrado. Verifique se o seletor CSS está correto.")

# # Fechar o navegador
# driver.quit()

# even_squares = []
# for x in range(10):
#     if x % 2 == 0:
#         even_squares.append(x**2)
# print(even_squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)