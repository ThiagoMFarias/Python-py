'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

contador = 0
cont = 0
for i in range(1,8):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('Você já atingiu a maioridade.')
        contador+=1
    else:
        print('Você ainda não atingiu a maioridade.')
        cont += 1

print('{} pessoas possuem a mrioridade'.format(contador))
print('{} pessoas ainda não atingiram a maioridade.'.format(cont))
