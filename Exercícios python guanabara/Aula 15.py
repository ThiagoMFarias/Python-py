cont = 1
<<<<<<< HEAD
while cont <= 10:
    print(cont, ' ', end = '')
    cont += 1
print('Acabou!')

n = 0
while n != 999:
    n = int(input('Digite um número: '))

n = cont= 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1
    
n = s = 0
while n !=999:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}.'.format(s))

n = s = 0
while n !=999:
    n = int(input('Digite um número: '))
    s += n
s -= 999 # Gambiarra
print('A soma vale {}.'.format(s))

# Loop infinito:
n = s = 0
while True:
    n = int(input('digite um número: '))
    s += n
print('A soma vale {}.'.format(s))

# Loop infinito com break:
n = s = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break # Quando eu dei esse comando, ele não contabiliza o 999 paea a soma.
    s += n
print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.') #PEP 498 que trata das fstrings mudou para essa forma de "printar". Esse "f" é a interpolação dentro de strings

nome = "Thiago"
idade = 38
salário = 1300.00
print('O {} tem {} anos.'.format(nome, idade))
print(f'O {nome} tem {idade} anos e ganha {salário:.2f} reais.') # Pyhton 3
print('O %s tem %d anos.' % (nome, idade)) # Python 2
=======
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
>>>>>>> 7e386b5a0b50c721ab3b2390de236c1f66b6df5e
