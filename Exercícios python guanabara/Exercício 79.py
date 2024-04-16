'''Crie um programa onde o usuário pode adicionar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''

num = []
while True:
    new_num = (int(input('Digite um valor: ')))
    if new_num in num:
        print('Esse número já existe. Por favor, digite outro número!')
    else:
        num.append(new_num)
        print('Valor adicionado com sucesso!')
    resp = ''
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou os valores {sorted(num)}!')  
      