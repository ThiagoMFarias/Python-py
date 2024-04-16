'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. no final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produto = ('Maçã', 15.82, 'Laranja', 8.93, 'Uva', 7.89, 'Banana', 3.49, 'Pêra', 6.97, 'Morango', 10.57)
print('-' * 50)
print(f'LISTAGEM DE PREÇO'.center(50))
print('-' * 50)

    
for item in range(0, len(produto)):
    if item % 2 == 0: # Perceba que o nome do produto está sempre numa posição par. 
        print(f'{produto[item]:.<42}', end = '')
    else:
        print(f'R$ {produto[item]:>5.2f}')

""" print(produto)
for item in produto:
    print(item)
for item in range(0, len(produto)):
    if item % 2 == 1: # Posição ímpar ele mostra só os preços 
        print(f'{produto[item]:30}') """