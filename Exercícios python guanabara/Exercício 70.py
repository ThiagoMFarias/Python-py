'''Crie um programa que leia o nome e o preço de vários produtos. Ele deverá perguntar se o usuário vai continuar. No final mostre:
A- qual o total gasto na compra;
B- quantos produtos custam mais de R$ 1.000,00;
C- Qual o nome do produto mais barato.'''

print('-------'*5)
print('          LOJA SUPER BARATÃO')
print('-------'*5)

tot = cont_prod = maior = menor = qtd_prod = 0
mais_barato = mais_caro = ''


while True:
    produto = input('Qual o nome do produto? ')
    price = float(input('Qual o valor do produto? R$ '))
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Digite uma resposta válida!')
    tot += price
    qtd_prod += 1

# A parte do código abaixo é para saber quantos produtos custam mais de mil reais.
    if price > 1000:
        cont_prod += 1

# A parte do código abaixo é para saber qual é o produto mais caro e o mais barato.
    if qtd_prod == 1:
        maior = menor = price
        mais_barato = mais_caro = produto
    else:
        if price > maior:
            maior = price
            mais_caro = produto
        if price < menor:
            menor = price
            mais_barato = produto

    if resp in 'Nn':
        break

print(f'O total da compra foi R$ {tot:.2f}.')
print(f'Temos {cont_prod} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi {mais_barato} que custa R$ {menor:.2f}.')
