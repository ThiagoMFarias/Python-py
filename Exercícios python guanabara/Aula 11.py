# Padrão ANSI de cores!!!

print('\033[0;30;mOlá, Mundo!')
print('\33[31mOlá, Mundo!')
print('\33[1;31;43mOlá, Mundo!\033[m')
print('\33[mOlá, Mundo!\33[m')
print('\33[37mOlá, Mundo!\33[m')

nome = 'Thiago'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\33[4;34m', nome, '\33[m'))

nome = 'Thiago'
cores = {'limpa': '\33[m',
         'azul': '\33[34m',
         'amarelo': '\33[32m',
         'pretoebranco': '\33[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores ['limpa']))
