# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:32:36 2022

@author: faria
"""

preço=float(input('Qual o preço do produto? R$ '))
desconto= preço - (5*preço/100)
print('O produto que custava R$ {:.2f}, com o desconto de 5% vai custar R$ {:.2f}'.format(preço, desconto))