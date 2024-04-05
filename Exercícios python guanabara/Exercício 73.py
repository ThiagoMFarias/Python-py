'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados;
b) os últimos 4 colocados da tabela;
c) uma lista com os times em ordem alfabética;
d) em que posição na tabela está o time da chapecoense.'''

times = ('Palmeiras', 'Grêmio', 'Atlético Mineiro', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atlético Paranaense', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corintians', 'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América Mineiro')

print(f'Os cinco primeiros colocados do brasileirão série A são {times[0:5]}.')
print(f'Os últimos colocados da tabela são {times[16:21]}')
print(f'Os times que participaram do Campeonato Brasileiro série A em 2023 foram {sorted(times)}')
print('O time da Chapecoense não se encontra jogando na série A do brasileirão.')
