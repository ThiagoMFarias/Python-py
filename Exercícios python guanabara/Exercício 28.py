import random

print('O computador está escolhendo um número entre 0 e 5...')
num = random.randrange(0, 5)
descubra = input("Digite qual número você acha que a máquina escolheu: ")

if descubra == num:
    print('Parabéns, o número escolhido pela máquina foi {}'.format(num))
    print('YOU WIM!')
else:
    print('A máquina escolheu o número {}'.format(num))
    print('YOU LOSE!')