'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = cont = soma = media = maior = menor = 0
resp = 'S'

# Posso fazer com while resp != 'N'
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = input('Quer continuar? [S/N]').upper().strip()
    
media = soma/cont
print('Você digitou {} números e a média entre eles é {}'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
    