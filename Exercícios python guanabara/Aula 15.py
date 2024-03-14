cont = 1
while cont < 10:
    print(cont, '->', end=' ')
    cont += 1
print(cont)
print('Acabou')

cont = 1
while cont <= 10:
    if cont == 10:
        print(cont, end= ' ')
    else:
        print(cont, '->', end=' ')
    cont +=1
print('Acabou')

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
# gambiarra para não somar com a flag (s -= 999)
print('A soma vale {}.'.format(s))

# sem a gambiarra de cima para não contar a flag:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'.format (s))
print(f'A soma vale {s}.') #Estou usando interpolação dentro de strings. Isso ocorre a partir do Python 3.

nome = 'Jesus'
idade = 33
salário = 1500.00
print(f'O {nome} tem {idade} anos.')
print('O %s tem %d anos.' %(nome, idade)) #Usado no Python 2!
print(f'O {nome} tem {idade} anos e ganha R$ {salário}.')
