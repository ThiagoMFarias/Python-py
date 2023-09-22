'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os Ns primeiros elementos de uma sequência de Fibonacci.'''

n = int(input('Insira um número: '))
print('==' * 10)
print('Calculando Fibonacci')
print('==' * 10)

termo1, termo2 = 0, 1
cont = 0
while cont <= n:
    if cont != n - 1:
        print('{} |'.format(termo1), end = ' ')
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
        cont += 1
    else:
        print('{}'.format(termo2))   