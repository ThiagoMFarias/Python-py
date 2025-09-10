cont = 1
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
