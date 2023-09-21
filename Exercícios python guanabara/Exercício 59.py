'''Crie um programa que leia dois valores e mostre um menu na tela: 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0

while menu != 5:
    menu = int(input('''\nAgora escolha quais das operações você deseja:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa\n'''))
    
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif menu == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multi))
    elif menu == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        elif n1 == n2:
            None
        else:
            None
    elif menu == 4:
        print('Insira novos valores: ')
        print(int(input('Insira o primeiro número: ')))
        print(int(input('Insira o segundo valor: ')))
    elif menu == 5:
        print('Finalizando...')
        break
    else:
        print('Opção inválida. Tente novamente.')

print('Obrigado pela sua participação! Volte sempre!')                 
                     