'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. NO final, moste quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = count = soma = 0
while True:
    num = int(input('Digite um número inteiro. Se quiser parar digite [999]. '))
    if num == 999:
        break
    count += 1
    soma += num

print(f'A soma dos {count} valores foi {soma}')
    