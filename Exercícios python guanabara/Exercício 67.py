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
