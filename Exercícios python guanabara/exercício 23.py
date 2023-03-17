# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:18:30 2023

@author: Thiago
"""

##faça um programa que leia um número de 0 a 9999 e mstre na tela cada um dos
#dígitos separados

numero = input('Digite um valor entre 0 a 9999:')
print(f'unidade:{numero[-1]}')
print(f'dezena:{numero[-2]}')
print(f'centena:{numero[-3]}')
print(f'milhar{numero[-4]}')

#outra forma de se formatar
print('São {} milhar'.format(numero[-4]))
print('São {} centena'.format(numero[-3]))
print('São {} dezena'.format(numero[-2]))
print('São {} unidades'.format(numero[-1]))