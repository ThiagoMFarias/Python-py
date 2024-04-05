<<<<<<< HEAD
'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. NO final, moste quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = count = soma = 0
while True:
    num = int(input('Digite um número inteiro. Se quiser parar digite [999]. '))
    if num == 999:
        break
    count += 1
    soma += num

print(f'A soma dos {count} valores foi {soma}')
    
=======
'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag)'''

cont = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
>>>>>>> 7e386b5a0b50c721ab3b2390de236c1f66b6df5e
