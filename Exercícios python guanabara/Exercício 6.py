# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
do = n1 * 2
tri = n1 * 3
rq = n1 ** (1/2)

print('O dobro do número {} é {}'.format(n1, do))
print('O triplo do número {} é {}'.format(n1, tri))
print('A raiz quadrada do número {} é {}'.format(n1, rq))