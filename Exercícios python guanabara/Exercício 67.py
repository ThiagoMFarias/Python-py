'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.''' 
import time

print('--' * 17)
print(' Bem vindo a TABUADA com laço WHILE.')
print('--' * 17)
while True:
    num = int(input('Digite qual número você gostaria de saber a tabuada: '))
    if num < 0:
        break
    for i in range (1, 11):
        print(f'{num} x {i} = {num * i}')
        
print('Você digitou um número negativo. O programa irá explodir...')
for contagem in range (5, 0, -1):
    print(contagem)
    time.sleep(1)
print('BUUUUUUUMMMMMMMMMMMMM........')
