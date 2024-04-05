'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint

print('=-' * 13)
print(' VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 13)

vitorias_consecutivas = 0
while True:
    num = int(input('Digite um valor: '))
    escolha = input('Você quer PAR ou ÍMPAR? [P/I] ').upper()
    comp = randint(1, 10)
    soma = comp + num    
    print(f'O computador jogou {comp} e você {num}.')
    
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'A soma entre os dois números é {soma} que é um número {resultado}.')
    
    if escolha == 'P' and resultado == 'PAR' or escolha == 'I' and resultado == 'ÍMPAR':
        print('Você venceu!')
        print('Vamos jogar novamente...')   
        vitorias_consecutivas += 1
    else:
        print('GAME OVER!')
        break
if 
print(f'Você ganhou {vitorias_consecutivas} vezes consecutivas.')    