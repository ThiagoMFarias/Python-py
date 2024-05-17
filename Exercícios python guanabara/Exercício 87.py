'''aprimore o desafio 86 mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.'''

# Preenchendo a matriz e calculando a soma dos valores pares
matriz = [[0,0,0], [0,0,0], [0,0,0]]
maior = soma_par = soma_col3 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]

# Calculando a soma dos valores da terceira coluna
for linha in range (0,3):
    soma_col3 += matriz[linha][2]

# Encontrando o maior valor da segunda linha
""" maior_segunda_linha = matriz[1][0]    
for valor in matriz[1]:
    if valor > maior_segunda_linha:
        maior_segunda_linha = valor """
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
        
# Imprimindo a matriz
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
    print() 

print(f'A soma de todos os valores da 3ª é {soma_col3}.')
print(f'O maior valor digitado da 2ª linha foi {maior}.')
