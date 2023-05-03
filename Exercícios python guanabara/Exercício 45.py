'''Crie um programa que faça o computador jogar Jokenpô com você:'''

import random
import time

print('{:=^40}'.format(' JOKENPÔ '))

# Criei uma lista com os seguintes objetos:
itens = ('Pedra', 'Papel', 'Tesoura')

# O usuário vai escolher um dos três objetos da lista.
escolha = int(input('Qual sua jogada?: \n [1] Pedra\n [2] Papel\n [3] Tesoura\n'))
print('-=' * 11)
print(' Você escolheu {}'.format(itens[escolha-1])) # Subtraí 1 já que a lista começa com índice 0.
print('-=' * 11)

# A máquina começa a "pensar" qual objeto da lista escolher.
print('-=' * 20)
print('O comutador está escolhendo como jogar...')
print('-=' * 20)
x = random.randint(0, 2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1) 
print('PÔ')
time.sleep(1)
print('-=' * 11)
print('O computador escolheu {}'.format(itens[x-1])) # Subtraí 1 já que a lista começa com índice 0.
print('-=' * 11)

if x == 0:
    if escolha == 0:
        print('EMPATE!')
    elif escolha == 1:
        print('VOCÊ VENCEU!')
    elif escolha == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida!')
elif x == 1:
    if escolha == 0:
        print('COMPUTADOR VENCEU!')
    elif escolha == 1:
        print('EMPATE!')
    elif escolha == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada inválida!')
elif x == 2:
    if escolha == 0:
        print('VOCÊ VENCEU!')
    elif escolha == 1:
        print('COMPUTADOR VENCEU!')
    elif escolha == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')
