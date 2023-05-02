''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final. de cordo com sua média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média7.0 ou superior: APROVADO'''

nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
media = float(nota_1 + nota_2)/2

if media < 5:
    print('Sua média é {}'.format(media))
    print("Estude mais. Você foi REPROVADO!")
elif 5 <= media <= 6.9:
    print('Sua média é {}'.format(media))
    print("Estude mais. Você está de RECUPERAÇÃO!")
else:
    print('Sua média é {}'.format(media))
    print('PARABÉNS! VOCÊ PASSOU DE ANO!')
    