'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta da inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

num = []

for cont in range(0,5):
    num.append(int(input('Digite um valor: ')))
    if cont == 0:
        print(f'Número {num[0]} foi adicionado ao final da lista.')
    if cont == 1:
        if num[1] > num[0]:
            print(f'O número {num[1]} foi adicionado ao final da lista.')
        else:
            print(f'O número {num[1]} foi adicionado ao início da lista.')
    if cont == 2:
        if num[2] > num[1]:
            print(f'O número {num[2]} foi adicionado no final da lista.')
        if num[2] < num[0]:
            print(f'O número {num[2]} foi adicionado no início da lista.')
        else: 
            print(f'O número {num[2]} foi adicionado ao índice 2.')
    if cont == 3:
        if num[3] > num[2]:
            print(f'O número {num[3]} foi adicionado ao final da lista.')
        if num[3] < num [0]: 
            print(f'O número {num[3]} foi adicionado ao início da lista.')
        if num[3] < num[1] and num[3] > num[0]:
            print(f'O número {num[3]} foi adicionado ao índice 1.')
        if num[3] < num[2] and num[3] > num[1]:
            print(f'O número {num[3]} foi adicionado ao índice 2.')
        else:
            print(f'O número {num[3]} foi adicionado ao índice 3.')
    if cont == 4:
        if num[4] > num[3]:
            print(f'O número {num[4]} foi adicionado ao final da lista.')
        if num[4] < num [0]: 
            print(f'O número {num[4]} foi adicionado ao início da lista.')
        if num[4] < num[1] and num[4] > num[0]:
            print(f'O número {num[4]} foi adicionado ao índice 1.')
        if num[4] < num[2] and num[4] > num[1]:
            print(f'O número {num[4]} foi adicionado ao índice 2.')
        if num[4] < num[3] and num[4] > num[2]:
            print(f'O número {num[4]} foi adicionado ao índice 3.')
print(num)     

