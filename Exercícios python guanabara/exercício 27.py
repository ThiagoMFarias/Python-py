# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:29:24 2023

@author: Thiago
"""

''' Faça um programa que leia o nome completo de uma pessoa, mostrando em 
seguida o primeiro e o último nome separadamente'''

nome = input('Digite seu nome completo: ')
primeiro_nome = nome.split()
a = len(nome)

print('O primeiro nome dessa pessoa é {}'.format(primeiro_nome[0]))

