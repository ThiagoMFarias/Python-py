'''Faça um programa que leia o nome e peso de várias pessoas. No final, mostre:
a) quantas pessoas foram cadastradas;
b) uma listagem com as pessoas mais pesadas;
c) uma listagem com as pessoas mais leves;'''

temp = list()
princ = list()
cont = maior = menor = 0
while True:
    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    cont +=1
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp in 'Nn':
        break
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi {maior}kg.', end = '')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end = '')
print()
print(f'O menor peso foi de {menor}kg. ', end = '')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')
