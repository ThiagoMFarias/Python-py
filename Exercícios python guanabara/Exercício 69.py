'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
A- quantas pessoas têm mais de 18 anos;
B- quantos homens foram cadastrados;
C- quantas mulheres tem menos de 20 anos.'''

print('-'*18)
print('CADASTRO POSITIVO')
print('-'*18)

cont_Idade = cont_Homem = cont_Mulher = 0
while True:
    idade = int(input('Qual a idade? '))
    sexo = ' '
    resp = ' '

    # Se a pessoa não digitar M ou F o programa vai continuar a perguntar novamente.
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('Digite uma resposta válida!')
    if idade > 18:
        cont_Idade += 1
    if sexo in 'Mm':
        cont_Homem += 1
    if sexo in 'fF' and idade < 20:
        cont_Mulher += 1
    
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0] #Uso o índice 0 no caso da pessoa digitar sim ou não por extenso. 
        if resp in 'Nn':
            break
        print('Digite uma resposta válida!')
    if resp in 'Nn': #Aqui tive que repetir o último comando para terminar o while da linha 11.
        break

print(f'O total de homens cadastrados foram {cont_Homem}.')
print(f'O total de pessoas com mais de 18 anos foram {cont_Idade}.')
print(f'O total de mulheres com menos de 20 anos foram {cont_Mulher}.')
    