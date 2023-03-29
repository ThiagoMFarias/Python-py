# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:18:30 2023

@author: Thiago
"""

# Faça um programa que leia um número de 0 a 9999 e mstre na tela cada um dos dígitos separados:

numero = int(input('Digite um valor entre 0 a 9999:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Esse código abaixo ele ta errado pois se eu digitar um número menor que 4 dígitos ele dá erro!
""" print(f'unidade:{numero[-1]}')
print(f'dezena:{numero[-2]}')
print(f'centena:{numero[-3]}')
print(f'milhar{numero[-4]}')

#outra forma de se formatar
print('São {} milhar'.format(numero[-4]))
print('São {} centena'.format(numero[-3]))
print('São {} dezena'.format(numero[-2]))
print('São {} unidades'.format(numero[-1])) """