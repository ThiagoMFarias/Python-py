# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:04:22 2023

@author: Thiago
"""

# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome

nome = str(input('Digite seu nome completo? ')).strip().title()

if 'Silva' in nome:
    print('Parabéns, você tem o sobrenome mais comum do Brasil!')
else:
    print('Seu nome completo é {}'.format(nome))

# Outro modo de fazer:

nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))
