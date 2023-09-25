'''Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
import time

print('-=' * 20)
print('O computador está escolhendo um número.')
print('-=' * 20)

num = randint(0, 11)
jogador = ''
palpites  = 0

while jogador != num:
    jogador = int(input('Tente adivinhar qual o número que o computador escolheu entre 0 e 10: '))
    print('PROCESSANDO...')
    time.sleep(1)
    if jogador == num:
        print('Parabéns! Você acertou o número que a máquina escolheu!')
    else: 
        print('Número errado. Tente novamente.')
        palpites += 1
           
print('O número escolhido pela máquina foi {}.'.format(num))

if palpites == 1:
    print('Você tentou {} vez até acertar.'.format(palpites))
else:
    print('Você tentou {} vezes até acertar.'.format(palpites))
