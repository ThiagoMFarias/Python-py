'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. NO final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

print('-='*20)
print(f'{"JOGO DO DADINHO":^39}')
print('-='*20)

jogo = {str(input('Primeiro jogador:').title()): randint(1,6),
        str(input('Segundo jogador: ').title()): randint(1,6),
        str(input('Terceiro jogador: ').title()): randint(1,6),
        str(input('Quarto jogador: ').title()): randint(1,6)}

ranking = list ()
print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
    