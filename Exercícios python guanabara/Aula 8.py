import math
from math import sqrt, ceil # Posso usar isso quando quero importar apenas alguns itens da biblioteca.
import random

'''Se eu for usar o "from" ao invés de "import" logo direto, quando eu chegar na parte de nomear uma variável, eu tenho que tirar a parte "math" antes da função que eu quero.'''

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz arredondada pra cima de {} é igual a {}'.format(num, math.ceil(raiz))) # Arredonda pra cima.
print('A raiz arredondada pra baixo de {} é igual a {}'.format(num, math.floor(raiz))) # Arredonda pra baixo.

# Número aleatório entre 0 e 1.
numero = random.random()
print(numero)

# Número aleatório entre vários valores:
núm = random.randint(1, 10)
print(núm)