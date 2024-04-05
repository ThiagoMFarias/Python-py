<<<<<<< HEAD
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
=======
'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

n = 0
while n >= 0:
    n = int(input('Digite um número que você queira saber a tabuada: '))
    if n < 0:
        print('Programa encerrado!')
        print('Você digitou um número negativo. ')
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n * i}')
    resp = input('Deseja outro número? [S/N] ')
    if resp in 'Nn':
        print('Obrigado e volte sempre!')
        break
>>>>>>> 7e386b5a0b50c721ab3b2390de236c1f66b6df5e
