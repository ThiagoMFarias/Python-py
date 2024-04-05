# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 16:10:57 2023

@author: Thiago
"""

'''Crie um programa que leia uma frase pelo teclado e mostre quantas vezes aperece a letra "A";  em que posição ela aperece a primeira vez; em que posição ela aparece pelo última vez'''

frase = str(input('Escreva uma frase: ')).strip().lower()
print(frase)

# if "A" or "a" in frase:   
#     print('A frase tem {} "as"'.format(frase.count('a')))

print('A frase têm {} de "A"'.format(frase.count("a")))
print('O primeiro "a" aparece no índice {}'.format(frase.find('a')))
print('O último "a" aparece no índice {}'.format(frase.rfind('a')))
