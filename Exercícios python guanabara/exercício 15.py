# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:46:23 2022

@author: faria
"""
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que  carro custa R$ 60 por dia e R$ 0,15 por km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
preço = km * 0.15 + 60 * dias
print('O total a pagar é R$ {:.2f}'.format(preço))
