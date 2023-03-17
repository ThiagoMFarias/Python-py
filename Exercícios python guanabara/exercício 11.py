# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:17:49 2022

@author: faria
"""
largura=float(input('Qual a largura da parede? '))
altura=float(input('Qual a altura da parede? '))
area= largura*altura
litros= area/2
print('A quantidade de tinta necessária para limpar a parede será de {:.2f}L'.format(litros))
