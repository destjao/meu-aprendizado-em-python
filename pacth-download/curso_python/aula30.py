'''
CONSTANTES = Variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
 <- contagem de complexidade
'''

velocidade = 59 # velocidade atual do carro
loc_car = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local aonde está o radar 1
RADAR_RANGE = 1 # A distância onde o radar pega


if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')
if loc_car >= (LOCAL_1 - RADAR_RANGE) and \
        loc_car <= (LOCAL_1 + RADAR_RANGE):
    print('Carro multado em radar 1')