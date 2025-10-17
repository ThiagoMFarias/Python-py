'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''

num = [int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), ]
print(f'O maior número da lista foi {max(num)} na posição {num.index(max(num)) + 1}.')
print(f'O menor valor digitado foi {min(num)} na posição {num.index(min(num)) + 1}.')

 # O código acima não elenca o problema de caso o usuário digite dois números iguais, o programa só imprimirá o primeiro deles.

# Segue agora a resposta do professor:

listanum = []
maior = menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {max(listanum)} na posição ', end= '')
for indice, valor in enumerate(listanum):
    if valor == maior:
        print(f'{indice}... ', end = ' ')

print(f'\nO menor valor digitado foi {menor} na posição ', end= '')
for indice, valor in enumerate(listanum):
    if valor == menor:
        print(f'{indice}...', end= '')
        break
    StopIteration
