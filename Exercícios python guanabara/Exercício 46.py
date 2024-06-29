''' Faça um programa que mostre na tela uma contagem regressiva para o estour de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

import time

for i in range(10, -1, -1): # o segundo '-1' é colocado porque eu queria que o contador fosse até 0. Se colocasse até 0, só iria até '1'.
    print(i)
    time.sleep(1)
print('======' * 3)
print(' FOGOS ESTOURANDO')
print('======' * 3)
