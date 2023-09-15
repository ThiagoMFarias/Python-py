# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha o segundo número: '))
num3 = int(input('Escolha o terceiro número: '))

if (num1 <= num2) and (num1 <= num3):
    if num2 <= num3:
        maior = num3
        menor = num1
        print('O maior número é {}'.format(maior))
        print('O menor número é {}'.format(menor))
    else:
        maior1 = num2
        menor1 = num1
        print('O maior número é {}'.format(maior1))
        print('O menor número é {}'.format(menor1))
else:
    if num3 >= num1 >= num2:
        maior2 = num3
        menor2 = num2
        print('O maior número é {}'.format(maior2))
        print('O menor número é {}'.format(menor2))

if num1 >= num2 and num1 >= num3:
    if num2 <= num3:
        maior3 = num1
        menor3 = num2
        print('O maior número é {}'.format(maior3))
        print('O menor número é {}'.format(menor3))
    else:
        maior4 = num1
        menor4 = num3
        print('O maior número é {}'.format(maior4))
        print('O menor número é {}'.format(menor4))
        