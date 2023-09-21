'''refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:'))
termo = int(input('Digite quantos termos você quer descobrir nessa PA: '))
print('A sequência dos {} primeiros termos dessa PA é '.format(termo), end='')
an = 1

while an < 11:
    if an == termo:
        print('{}'.format(a1 + (an - 1) * r), end = ' ')
    else:
        print('{} |'.format(a1 + (an - 1) * r), end = ' ')
    an += 1
