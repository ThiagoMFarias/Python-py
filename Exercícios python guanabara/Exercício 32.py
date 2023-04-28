# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um ano qualquer ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Esse ano, {}, é bissexto!'.format(ano))
else:
    print('Esse ano, {}, não é bissexto!'.format(ano))