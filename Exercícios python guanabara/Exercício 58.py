'''Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
import time

print('-=' * 20)
print('O computador está escolhendo um número.')
print('-=' * 20)

num = randint(0, 11)
jogador = ''
cont = 0

while jogador != num:
    jogador = int(input('Tente adivinhar qual o número que o computador escolheu entre 0 e 10: '))
    print('PROCESSANDO...')
    time.sleep(1)
    cont += 1
    if jogador == num:
        print('Parabéns! Você acertou o número que a máquina escolheu!')
        
print('O número escolhido pela máquina foi {}.'.format(num))

if cont == 1:
    print('Você tentou {} vez até acertar.'.format(cont))
else:
    print('Você tentou {} vezes até acertar.'.format(cont))
