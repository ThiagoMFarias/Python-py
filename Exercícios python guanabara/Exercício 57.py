'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o sexo da pessoa? ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido. Por favor, digite "M" para masculino ou "F" para feminino')
    
print('Parabéns! Seu código funciona!')
print('Sexo válido:', sexo)
