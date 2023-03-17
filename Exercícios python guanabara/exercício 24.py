# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:52:06 2023

@author: Thiago
"""

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não 
# com nome 'Santo"

city = input('Digite o nome de uma cidade: ')

if city[0:5] == 'Santo':
    print('O nome da cidade começa com Santo')
else: 
    print('O nome da cidade é {}'.format(city))