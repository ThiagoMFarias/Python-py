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
