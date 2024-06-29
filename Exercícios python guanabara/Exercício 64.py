'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flog).'''

num = cont = soma = 0
num = int(input('Digite um número: Se quiser parar digite 999. '))
while num != 999:
    num = int(input('Digite um número: Se quiser parar digite 999. '))
    soma += num
    cont += 1
    
print('A soma de todos os números digitados foi {}.'.format(soma - 999))
print('Você digitou {} números.'.format(cont - 1))
