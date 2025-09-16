'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

while True:
    expressao = str(input('Digite a expressão que você quer averiguar: '))
    if expressao.count('(') == expressao.count(')'):
        print('Sua expressão está válida!')
    else:
        print('Sua expressao está errada!')
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
        