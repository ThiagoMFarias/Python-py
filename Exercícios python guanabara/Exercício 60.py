'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

from math import factorial
n = int(input('Insira um número e descubra qual o valor do fatorial dele: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

# Outra forma de fazer:
m = int(input('Insira um número e descubra qual o valor do fatorial dele: '))
cont = m
g = 1 # Fator nulo num fatorial
print('Calculando {}! = '.format(m), end ='')
while cont > 0:
    print('{} x '.format(cont), end=' ')
    if cont == 1:
        print('= ', end = '')
    g *= cont
    cont -= 1

print('{}'.format(g))
