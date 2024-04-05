'''crie um programa que simule o funcionamento de um caixa eletrõnico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''

print('-'*30)
print('{:^30}'.format('BANCO FVA'))
print('-'*30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0 # isso é o total de cédulas 
while True:
    if total >= céd:
        total -= céd
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'O total de cédulas de R$ {céd} é {totcéd}. ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if totcéd == 0:
            break
        
""" while True:
    if valor > 50:
        resto50 = valor % 50
        resultado = int(valor//50)
        print(f'Você receberá {resultado} cédulas de R$ 50.')
        if resto50 > 20:
            resto20 = resto50 % 20
            resultado20 = int(resto50//20)
            print(f'Você recebrá {resultado20} cédulas de R$ 20.')
            if resto20 >10:
                resto10 = resto20 % 10
                resultado10 = int(resto20//10)
                print(f'Você receberá {resultado10} cédulas de R$ 10.')
                if resto10 > 1:
                    resto1 = resto10 % 1
                    resultado1 = int(resto10//10) """
# if valor == 50:
#     print('Total de 1 cédula de R$ 50')
# if valor == 20:
#     print('Total de 1 cédula de R$ 20')
# if valor == 10:
#     print('Total de 1 cédula de R$ 10')
# if valor == 1:
#     print('Total de 1 cédula de R$ 1')
