# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:26:11 2022

@author: faria
"""
# Informe a temperatura em ºC: 

temp = float(input('Informe a temperatura em ºC: '))
fahr = (temp*1.8) + 32
print('A temperetura de {}ºC corresponde a {:.2f}ºF!'.format(temp, fahr))
print('A temperatura de {}ºC corresponde a {}ºF!'.format(temp, (temp*1.8)+32))
