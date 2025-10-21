'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que matenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

princ = list()
par = list()
impar = list()

for p in range(1, 8):
    num = int(input(f'Digite {p}º valor: '))
    if  num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
princ.append(par[:])
princ.append(impar[:])
par.clear()
impar.clear()
print(f'Os valores pares digitados foram {sorted(princ[0])}.')
print(f'Os valores ímpares digitados foram {sorted(princ[1])}.')

'''Resolução do professor:
num = [[], []]
valor = 0
for c in range (1, 8):
    valor = int (input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-= * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}.')
print(f'Os valores ímpares digitados foram {num[1]}.')'''
