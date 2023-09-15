'''Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa mostre: 
1- A média de idade do grupo;
2- Qual é o nome do homem mais velho;
3- E quantas mulheres têm menos de 21 anos.'''

for i in range(1,5):
    nome = input('Qual o seu nome? ')
    sexo = input('Qual o seu sexo? [M] para mulher e [H] para homem. ').upper()
    idade = int(input('Qual a sua idade? '))
