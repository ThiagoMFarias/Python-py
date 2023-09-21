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

resposta = print('\nsaaasasaa')
