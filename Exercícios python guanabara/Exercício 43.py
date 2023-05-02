'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule  IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5: ABAIXO DO PESO;
- Entre 18.5 e 25: PESO IDEAL;
- Entre 25 e 30: SOBREPESO;
- Entre 30 e 40: OBESIDADE;
- Acima de 40: OBESIDADE MÓRBIDA'''

print('=-=-=' * 8)
print('   Bem vindo(a) ao seu CÁLCULO DE IMC')
print('=-=-=' * 8)

altura = float(input('Digite aqui sua altura: '))
peso = float(input('Digite aqui seu peso em kg: '))
imc = peso/pow(altura, 2)
print('_____')
print('{:.2f}'.format(imc))
print('¨¨¨¨¨')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
    