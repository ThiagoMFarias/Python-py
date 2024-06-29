'''Refaça o exercício 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isóceles: dois lados iguais;
- Escaleno: todos os lados diferentes.'''

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da primeira reta: '))
reta3 = float(input('Digite o valor da primeira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triângulo.')
    if reta1 == reta2 == reta3:
        print('Você acabou de formar um triângulo EQUILÁTERO.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Você acaba de criar um triângulo ISÓCELES.')
    else:
        print('Você acaba de formar um triângulo ESCALENO.')
else:
    print('As retas digitadas não formam um triângulo.')

''' Posso fazer dessa outra forma: 
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas podem formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO.')
    if reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('ISÓCELES.')
    if reta1 != reta2 != reta3 !=reta1:
        print('ESCALENO.')
else:
    print('As retas digitadas não formam um triângulo.')'''
    