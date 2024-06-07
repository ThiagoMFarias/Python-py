'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

aluno = []
temp_aluno = []

print('-=' * 30)

while True:
    temp_aluno.append(str(input('Qual o nome do aluno? ')).title())
    temp_aluno.append(float(input('Qual a 1ª nota? ')))
    temp_aluno.append(float(input('Qual a 2ª nota? ')))
    media = temp_aluno.append((temp_aluno[1] + temp_aluno[2]) / 2)
    aluno.append(temp_aluno[:])
    temp_aluno.clear()
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()
    if resp in 'Nn':
        break
    
print('-=' *30)
print(f'{"Nº":<4}{"NOME":^25}{"MÉDIA":>8}')

print('-'*40)
for c in range(0, len(aluno)):
    print(f'{c:<4}{aluno[c][0]:^25}{aluno[c][3]:>7.1f}')
    
print('-'*40)
num = int(input('Você gostaria de saber as notas de qual aluno? [DIGITE O NÚMERO DO ALUNO] '))
print(f'As notas do(a) aluno(a) {aluno[num][0]} são {aluno[num][1]} e {aluno[num][2]}.')

#Resolução do professor

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #Note que aqui ele não criou outra lista, apenas inseriu, individualmente, cada nota dentro da lista ficha.
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-' * 26)

for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Quer mostar a nota de quais alunos? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('<<<VOLTE SEMPRE>>>')
