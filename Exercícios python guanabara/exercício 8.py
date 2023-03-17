# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:46:21 2022

@author: faria
"""
# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input("Digite uma distância em metros: "))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print("A medida equivale a {} km, em hectômetro é {} hm, em decâmetro é {} dam, em decímetro é {} dm, em centímetro é {} cm e em milímetros é igual a {} mm".format(km, hm, dam, dm, cm, mm))