'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais.'''

ent = int(input('Digite o primeiro número inteiro: '))
ent1 = int(input('Digite o segundo número inteiro: '))

if ent > ent1:
    print('O primeiro valor é o maior.')
elif ent < ent1: 
    print('O segundo valor é o maior.')
else:
    print('Os dois valores são iguais.')