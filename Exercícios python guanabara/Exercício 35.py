# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da primeira reta: '))
reta3 = float(input('Digite o valor da primeira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas digitadas não formam um triângulo.')
    