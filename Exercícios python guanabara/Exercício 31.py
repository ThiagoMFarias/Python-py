# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem em km?'))
preco1 = distancia * 0.5
preco2 = distancia * 0.45
if distancia <= 200:
    print('O preço da passagem será R$ {}'.format(preco1))
else: 
    print('O preço da passagem será R$ {}'.format(preco2))
