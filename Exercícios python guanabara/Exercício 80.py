'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta da inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

num = []
maior = menor = 0

for cont in range(0,5):
    num.append(int(input('Digite um valor: ')))

for c, n in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}')
