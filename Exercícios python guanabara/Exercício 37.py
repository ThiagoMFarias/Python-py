'''Escreva um programa que leia um npumero inteiro qualquer e peça para o usuário escolher qual será a base de conversão'''

ent = int(input("Digite um número qualquer: "))
esc = str(input('''Agora digite:
                [1] para conversão binária
                [2] para conversão octal 
                [3] para conversão hexadecimal: \n'''))

if esc == '1':
    print('O número {} em binários é {}.'.format(ent, str(bin(ent)[2:])))
elif esc =='2':
    print('O número {} em octal é {}.'.format(ent, format(str(oct(ent)[2:]))))
elif esc =='3':
    print('O número {} em octal é {}.'.format(ent, format(str(hex(ent)[2:]))))
else:
    print('Opção inválida!')
    