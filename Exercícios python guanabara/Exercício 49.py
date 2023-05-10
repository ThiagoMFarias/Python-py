'''refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora com laço for.'''

print('--' * 17)
print(' Bem vindo a TABUADA com laço FOR.')
print('--' * 17)
n = int(input('Qual número você quer saber a tabuada? \n'))
for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))