'''Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa mostre: 
1- A média de idade do grupo;
2- Qual é o nome do homem mais velho;
3- E quantas mulheres têm menos de 21 anos.'''
from datetime import date

somaidade = 0
media_idade = 0
maior_idade_homem= 0
nome_velho = ''
total_mulher20 = 0

for pessoa in range(1,5):
    print('----- {}ª PESSOA -----'.format(pessoa))
    nome = input('Qual o seu nome? ').strip()
    sexo = input('Qual o seu sexo? [M] para mulher e [H] para homem. ').upper().strip()
    idade = int(input('Qual a sua idade? '))
    somaidade += idade
    if pessoa == 1 and sexo in 'Hh':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Hh' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade < 21:
        total_mulher20 += 1

media_idade = somaidade/4
print('A média da idade do grupo é {}'.format(media_idade))
print('O homem mais velho é o {} e sua idade é de {} anos.'.format(nome_velho, maior_idade_homem))
print('O total de mulheres menores que 20 anos são {}.'.format(total_mulher20))
