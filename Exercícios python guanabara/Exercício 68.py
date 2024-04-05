<<<<<<< HEAD
'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint

print('=-' * 13)
print(' VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)

vitorias_consecutivas = 0
while True:
    num = int(input('Digite um valor: '))
    escolha = input('Você quer PAR ou ÍMPAR? [P/I] ').upper()
    comp = randint(1, 10)
    soma = comp + num    
    print(f'O computador jogou {comp} e você {num}.')
    
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'A soma entre os dois números é {soma} que é um número {resultado}.')
    
    if escolha == 'P' and resultado == 'PAR' or escolha == 'I' and resultado == 'ÍMPAR':
        print('Você venceu!')
        print('Vamos jogar novamente...')   
        vitorias_consecutivas += 1
    else:
        print('GAME OVER!')
        break
if 
print(f'Você ganhou {vitorias_consecutivas} vezes consecutivas.')    
=======
'''Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando a soma entre o número escolhido pelo jogador e o computador for diferente da resposta Par ou Ímpar do jogador. Mostre também o total de vitórias consecutivas que ele conquistou no final do jogo.'''

import random

print('-'*30)
print('Bem vindo ao jogo PAR OU ÍMPAR')
print('-'*30)
print('\nNessa experiência incrível você irá jogar contra o computador para tentar adivinhar se o número que ele jogou é PAR OU ÍMPAR.')

cont = 0
while True:
    num = int(input('Digite um número: '))
    escolha = input('Você acha que o computador irá escolher PAR OU ÍMPAR? [P/I] ')
    print('O computador está escolhendo um número...')
    choice = random.randint(1,10)
    soma = num + choice 
    if soma % 2 == 0:
        print(f'Você jogou {num} e o comptador escolheu o número {choice}. Total deu {soma}.')
        print(f'{soma} é PAR.')
        cont += 1
        if escolha in 'Ii':
            break
    else:
        print(f'Você jogou {num} e o comptador escolheu o número {choice}. Total deu {soma}.')
        print(f'{soma} é ÍMPAR.')
        cont += 1
        if escolha in 'Pp':
            break

if cont == 1:
    print(f'GAME OVER! Você venceu {cont} vez.')
else:
    print(f'GAME OVER! Você venceu {cont} vezes.')
>>>>>>> 7e386b5a0b50c721ab3b2390de236c1f66b6df5e
