dados = list()
pessoas = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas.append(dados[:]) # fatiamento completo

# Listas compostas
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = list()
teste.append('Thiago')
teste.append(39)
galera = list()
galera.append(teste[:]) # 
teste[0] = 'Maria'
teste[1] = 34
galera.append(teste[:])
print(galera)

galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera1)
print(galera1[0])
print(galera1[0][0])
print(galera1[2][1])
for pessoa in galera1:
    print(pessoa)
for pessoa in galera1:
    print(pessoa[0])
for pessoa in galera1:
    print(pessoa[1])
for pessoa in galera1:
    print(f'{pessoa[0]} têm {pessoa[1]} anos.')

galera2 = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:]) # Se eu esquecer dos dois pontos, a lista vai aparecer vazia já que eles estão ligados.
    dado.clear() # Limpa a lista para a próxima iteração
print(galera2)
for pessoa in galera2:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade!')
