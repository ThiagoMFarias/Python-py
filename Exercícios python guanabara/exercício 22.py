# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 13:40:20 2023

@author: Thiago
"""

'''Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas;
# o nome com todas asletras minúsculas;
# quantas letras ao todo sem considerar espaços;
# quantas letras têm o primeiro nome;'''

nome = str(input('Qual o seu nome completo?')).strip()
space = nome.count(' ')

print(nome.upper())    
print(nome.lower())

print(space)
print('O seu nome têm {} letras'.format(len(nome)-space))

primeiro_nome = nome.split()
print('Seu primeiro nome têm {} letras'.format(len(primeiro_nome[0])))
