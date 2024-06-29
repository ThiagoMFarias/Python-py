'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. NO final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint

jogadores = dict()
jogadas = list()
maior = menor = 0
print('-='*20)
print(f'{"JOGO DO DADINHO":^39}')
print('-='*20)

for c in range(0,4):
    jogadores['NOME'] = str(input('Qual o nome do primeiro jogador? ').title())
    num = randint(1,6)
    if c == 0:
        maior = num
    else:
        if num >= maior:
            maior = num
    jogadores['JOGADA'] = num
    jogadas.append(jogadores.copy())
    
print(f'{dict(sorted(jogadores.items(),))}')
print(maior)