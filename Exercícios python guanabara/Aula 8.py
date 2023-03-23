import math
from math import sqrt, ceil # posso usar isso quando quero importar apenas alguns itens da biblioteca.
import random

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz arredondada pra cima de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz arredondada pra baixo de {} é igual a {}'.format(num, math.floor(raiz)))

# Número aleatório entre 0 e 1.
numero = random.random()
print(numero)

# número aleatório entre vários valores:
núm = random.randint(1, 10)
print(núm)