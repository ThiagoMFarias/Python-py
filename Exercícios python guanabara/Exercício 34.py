# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para valores superiores a R$ 1.250,00, calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o valor do seu salário? R$ '))
aum1 = (15*sal/100)
aum2 = (10*sal/100)

if sal <= 1250:
    print('Você terá um aumento de R$ {:.2f} no seu salário.'.format(aum1))
else:
    print('Você terá um aumento de R$ {:.2f} no seu salário.'.format(aum2))