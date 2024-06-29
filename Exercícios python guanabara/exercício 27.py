# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:29:24 2023

@author: Thiago
"""

''' Faça um programa que leia o nome completo de uma pessoa, mostrando em  seguida o primeiro e o último nome separadamente'''

nome = str(input('Digite seu nome completo: ')).strip().split()

print('O primeiro nome dessa pessoa é {}'.format(nome[0]))
print('O último nome da pessoa é {}'.format(nome[len(nome)-1]))
