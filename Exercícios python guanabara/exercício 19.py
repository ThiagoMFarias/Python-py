import random

print('O nome dos alunos são  respectivamente: Camila, Fábio, Thiago, Rebecca, Júnior, Débora')
alunos = random.randint(1, 6)

if alunos == 1:
    print('A aluna escolhida foi Camila')

if alunos == 2:
    print('A aluna escolhida foi Rebecca')

if alunos == 3:
    print('A aluna escolhida foi Débora')

if alunos == 4:
    print('O aluno escolhido foi Fábio')

if alunos == 5:
    print('O aluno escolhido foi Thiago')

if alunos == 6:
    print('O aluno escolhido foi Júnior')

# Outra maneira de fazer é:    
import random

a1 = str(input('Digite  primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))