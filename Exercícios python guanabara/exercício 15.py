# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:46:23 2022

@author: faria
"""

dias= int(input('Quantos dias alugados? '))
km= float(input('Quantos quilômetros rodados? '))
preço= km*0.15 + 60*dias
print('O total a pagar é R$ {:.2f}'.format(preço))