distancia = float(input('Qual a distância da viagem em km?'))
preco1 = distancia * 0.5
preco2 = distancia * 0.45

if distancia <= 200:
    print('O preço da passagem será R$ {}'.format(preco1))
else: 
    print('O preço da passagem será R$ {}'.format(preco2))
