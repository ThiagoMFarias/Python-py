'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta da inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []

for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]: # esse termo seria o úçtimo da lista. Posso fazer assim lista[len(lista - 1)].
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]: #Verifico se o número que eu vou inserir é menor ou igual a ele.
                lista.insert(pos, num)
                print(f'Adicionado a posição {pos} da lista.')
                break
            pos += 1
print('-=' * 22)
print(f'Os valores digitados foram {lista}.')     
