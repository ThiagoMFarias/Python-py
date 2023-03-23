import math

num = float(input('Digite um número real: '))

# Também posso usar a função math.trunc para exibir a parte inteira do número. 
print('O número digitado foi {} e tem a parte inteira igual a {}'.format(num, math.floor(num)))

# Outra frma de fazer é:
from math import trunc
num = float(input('Digite um número real: '))
print('O número digitado foi {} e tem a parte inteira igual a {}'.format(num, trunc(num)))

num = float(input('Digite um úmero: '))
print('O número digitado foi {} e sua parte inteira é {}'.format(num, int(num)))