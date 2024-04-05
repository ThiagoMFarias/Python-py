num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
tupla = (num1, num2, num3, num4)
print(f'Você digitou os valores {tupla}.')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 foi digitado no índice {tupla.index(3)}.')
else:
    print('O valor 3 não foi digitado.')

# Lista para armazenar números pares
numeros_pares = []

for numero in tupla:
    if numero % 2 == 0:
        numeros_pares.append(numero)

# Imprimir os números pares em uma linha
print(f'Os números pares digitados foram: {", ".join(map(str, numeros_pares))}.')
