'''Escreva um programa para aprovar o empréstimo bancário para comprar uma casa. Ele vai perguntar o valor da casa, o salário do comprador, e em quantos anos ele vai pagar. Calcule o valor da prestação mnsal, sabendo que ela não pode ultrapassar 30% do slário ou então o empréstimo será negado.'''

print('=======' * 10)
print('           Bem vindo(a) ao Programa Seu Dinheiro Minha Casa!')
print('=======' * 10)
valor = float(input('Por gentileza, qual o valor da casa que você deseja comprar? R$ '))
sal = float(input('Agora digite quanto você recebe por mês: R$ '))
anos = int(input("Em quantos anos você pretende pagar o financiamento? "))
prestacao = float(valor/(anos * 12))

if prestacao >= 0.3 * sal:
    print('Infelizmente seu empréstimo foi negado.')
else: 
    print('Parabéns, você acaba de adiquirir sua casa prórpria com prestações mensais de R$ {:.2f}.'.format(prestacao))
    