'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os Ns primeiros elementos de uma sequência de Fibonacci.'''

n = int(input('Insira um número: '))
print('==' * 10)
print('Calculando Fibonacci')
print('==' * 10)

ultimo, penultimo = 1, 1
if (n == 1) or (n == 2):
    print('O valor do fibonacci é "1".')
else:
    cont = 3
    while cont <= n:
        print('{} |'.format(penultimo), end = ' ')
        proximo_termo = penultimo + ultimo
        penultimo = ultimo
        ultimo = proximo_termo
        cont += 1
    print('{}'.format(proximo_termo))