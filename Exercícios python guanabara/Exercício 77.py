'''Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
import time

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

print('--'*30)
print(f'Analisando a quantidade de vogal em cada palavra da tupla...'.center(60))
print('--'*30)
time.sleep(2)

for vogais in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[vogais].upper()} temos ', end = ' ')
    for letra in palavras[vogais]:
        if letra in 'AEIOUaeiou':
            print(letra, end = ' ') 
            