# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:18:54 2022

@author: faria
"""

salário= float(input('Qual o salário do funcionário? R$ '))
aumento= salário + (15*salário/100)
print('O novo salário do funcionário com o aumento é de R$ {:.2f}'.format(aumento))

