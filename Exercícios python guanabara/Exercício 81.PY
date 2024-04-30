'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: 
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado ou não na lista.'''

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}.')
print(f'Você digitou {cont} números.')
if 5 in lista:
    for pos, valor in enumerate(lista):
        if valor == 5:
            print(f'O número 5 foi digitado na posição {pos}.')
else:
    print('O 5 não faz parte da lista.')
    