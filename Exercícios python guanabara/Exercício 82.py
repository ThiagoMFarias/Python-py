'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listasgeradas.'''

lista = []
lista_par = []
lista_ímpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if resp in 'Nn':
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        lista_par.append(lista[c])        
    else:
        lista_ímpar.append(lista[c])
print(f'Você digitou aos números {lista}.') 
print(f'Os números pares digitados foram {lista_par}.')
print(f'Os números ímpares digitados foram {lista_ímpar}.')
