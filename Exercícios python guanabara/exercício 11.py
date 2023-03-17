# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:17:49 2022

@author: faria
"""

# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
litros = area/2
print('A quantidade de tinta necessária para limpar a parede será de {:.2f}L'.format(litros))
