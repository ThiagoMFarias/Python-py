'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = input('Digite uma frase: ').strip().lower().split()
junto = ''.join(frase)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso+=junto[letra]
if junto == inverso:
    print('A frase escrita é um PALÍNDROMO.')
else:
    print('A frase escreita não é um PALÍNDROMO.')

''' Posso fazer sem o FOR também:

frase = input('Digite uma frase: ').strip().lower().split()
junto = ''.join(frase)
inverso = junto[::-1] 

if inverso == junto:
    print('A frase escrita é um palíndromo.')
else:
    print('A frase escrita não é um palíndromo')'''
