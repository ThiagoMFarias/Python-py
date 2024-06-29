# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:18:54 2022

@author: faria
"""
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento. 

salario = float(input('Qual o salário do funcionário? R$ '))
aumento = salario + (15*salario/100)
print('O salário do funcionário que era R$ {:.2f}, com o aumento passará a ganhar R$ {:.2f}'.format(salario, aumento))
