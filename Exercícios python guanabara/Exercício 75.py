'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) quantas vezes apareceu o número 9;
b) em que posição foi digitado o primeiro valor 3;
c) quais foram os números pares.'''

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o quarto valor: '))

tupla = (num1, num2, num3, num4)
print(f'Você digitou os valores {tupla}')

print(f'O número 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O número 3 foi digitado no índice {tupla.index(3)}.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

for cont in range(0, len(tupla)):
    if tupla[cont] % 2 == 0:
        print(f'Os números pares digitados foram {tupla[cont]}.')
        
# ...existing code...
# pares = tuple(num for num in tupla if num % 2 == 0)
# if pares:
#     print(f'Os números pares digitados foram: {pares}')
# else:
#     print('Nenhum número par foi digitado.')
# ...existing code...