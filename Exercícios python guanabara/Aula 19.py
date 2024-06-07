dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

# Dicionários
dados1 = {'nome':'Thiago', 'idade':39}
print(dados1 ['nome'])
print(dados1['idade'])
dados1['sexo'] = 'M' #Aqui eu não consigo usar o append para adicionar outro item ao meu dicionário. Preciso usar essa forma.
print(dados1)
del dados1['idade']
print(dados1)

filme = {'título': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
        }
filme1 = {'título': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whedon'
         }
filme2 = {'título': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachawski'   
         }
print(filme.values()) #Mostro todos os dados do dicionário
print(filme.keys()) #Mostro todos os índices(keys)
print(filme.items()) #Mostro todos os valores das chaves

for keys, values in filme.items(): # para cada chave e valor no filme.items eu vou fazer...
    print(f'O {keys} é {values}.')

for item in filme.items():
    print(item)
for item in filme:
    print(values)

'''Por que eu preciso usar filme.items() e não apenas filme?
Em Python, o método items() é usado para retornar uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionário. Isso é útil quando você deseja iterar tanto pelas chaves quanto pelos valores de um dicionário em um loop for. No seu exemplo, você está iterando sobre as chaves e os valores do dicionário filme usando o método items(). Se você usar apenas filme no loop for, você estará iterando apenas sobre as chaves, não sobre os pares chave-valor.
Por exemplo, se você fizer:
for item in filme:
    print(item)
Você verá apenas as chaves do dicionário filme, não os valores associados a essas chaves.
Por outro lado, se você fizer:
for item in filme.items():
    print(item)
Você obterá todas as tuplas chave-valor do dicionário filme, permitindo que você acesse tanto as chaves quanto os valores correspondentes dentro do loop.'''
    
# Eu posso criar uma lista com um dicionário dentro

locadora = list()
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
print(locadora)
print(locadora[0].values())
print(locadora[0]['ano'])
print(locadora[2]['título'])

pessoas = {'nome': 'Thiago', 'sexo': 'M', 'idade': 39}
print(pessoas)
#print(pessoas[0]) aqui da erro pois eu não tenho índice e sim chave, pois o elemento 0 é um nome.
print(pessoas['nome'])
print(f'O {pessoas["nome"]} têm {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Verlene'
pessoas['peso'] = 50.8
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k.title()} = {v}')
    if k in 'peso':
        print(f'{k.title()} = {v}kg.')

# Colocando um dicionário dentro de uma lista:
brasil = []
estado = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado)
brasil.append(estado1)
print(estado)
print(estado1)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])

país = list()
state = dict()
for c in range(0,3):
    state['uf'] = str(input('Digite um Estado: ')).title()
    state['sigla'] = str(input('Digite a sigla: ')).upper()
    país.append(state.copy()) #lembrando que eu não posso fazer fatiamento [:] num dicionário. Eu devo usar o método .copy().
print(país)
for e in país:
    print(e)
for e in país: # Esse for de fora é da lista.
    for k, v in e.items(): # esse for de dentro é do dicionário
        print(f'O campo {k} tem valor {v}')
         