from random import shuffle

a1 = str(input('Digite o preiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Gigite o quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem sorteada foi {}'.format(lista))
