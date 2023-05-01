'''Crie um programa que faça o computador jogar Jokenpô com você:'''

import random
import time

print('=======')
print('JOKENPÔ')
print('=======')

# Criei uma lista com os seguintes objetos:
lista = ['pedra', 'papel', 'tesoura']

# O usuário vai escolher um dos três objetos da lista.
escolha = int(input('Escolha: \n [1] Pedra\n [2] Papel\n [3] Tesoura\n').capitalize())

# Subtraí 1 já que a lista começa com índice 0. 
opcao = lista[escolha - 1]
print('Você escolheu {}'.format(opcao))

# A máquina começa a "pensar" qual objeto da lista escolher.
print('O comutador está escolhendo como jogar...')
time.sleep(2) 
x = random.choice(lista).capitalize()
print(x)

if opcao == x:
    print('O jogo deu empate. Jogue novamente.')
    lista = ['pedra', 'papel', 'tesoura']
    escolha = int(input('Escolha: \n [1] Pedra\n [2] Papel\n [3] Tesoura\n'))
    opcao = lista[escolha - 1]
    print('Você escolheu {}'.format(opcao))
    print('O comutador está escolhendo como jogar...')
    time.sleep(2) 
    x = random.choice(lista).capitalize()
    print(x)
    

if escolha == lista[0] and x == lista[1]:
    print('O computador venceu!')

if escolha == lista[0] and x == lista[2]:
    print('Você venceu. Parabéns!')

if escolha == lista[1] and x == lista[0]:
    print('Você venceu. Parabéns!')

if escolha == lista[1] and x == lista[2]:
    print('O computador venceu!')

if escolha == lista[2] and x == lista[0]:
    print('O computador venceu!')

if escolha == lista[2] and x == lista[1]:
    print('Parabéns. Você venceu!')