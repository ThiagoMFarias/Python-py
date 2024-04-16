'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''

num = [int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), ]
print(f'O maior número da lista foi {max(num)} na posição {num.index(max(num)) + 1}.')
print(f'O menor valor digitado foi {min(num)} na posição {num.index(min(num)) + 1}.')
