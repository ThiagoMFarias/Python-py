'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = int(input('Digite quantos termos você ver nessa PA: '))
print('A sequência dos {} primeiros termos dessa PA é '.format(termo), end = ' ')
an = 1

while an <= termo:
    if an == termo:
        print('{}'.format(a1 + (an - 1) * r), end = ' ')
    else:
        print('{} |'.format(a1 + (an - 1) * r), end = ' ')
    an += 1

resposta = str(input('\nVocê deseja mostrar mais termos dessa PA? [S/N]')).upper()

while resposta != 'N':
    if resposta == 'S':
        cont = 0 
        num = int(input('Quantos termos a mais você gostaria de visualizar dessa PA? '))
        for cont in range(0, num):
            if cont + 1 == num:
                print('{}'.format(a1 + (an - 1) * r), end = ' ')
                an += 1
            else:
                valor = '{} |'.format(int(a1 + (an - 1) * r))
                print(valor, end = ' ')
                cont += 1
                an += 1
        resposta = str(input('\nVocê deseja mostrar mais termos dessa PA? [S/N]')).upper()
print('Obrigado pela colaboração!')
           