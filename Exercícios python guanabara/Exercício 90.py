'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. NO final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()

aluno['NOME'] = str(input('Qual o nome do aluno? ')).title()
aluno['MÉDIA'] = float(input('Qual a média do aluno? '))
print(f'O nome do aluno(a) é {aluno["NOME"]}.')
print(f'A média é {aluno["MÉDIA"]}.')
if aluno['MÉDIA'] >= 7:
    print('Parabéns. Você foi aprovado!')
else:
    print('REPROVADO!!!!!!')
