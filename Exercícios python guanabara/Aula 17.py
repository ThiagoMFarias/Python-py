# Listas são mutáveis.

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'picolé'
print(lanche)

# Adicionando novos itens a lista:
lanche.append('cookie')
print(lanche)

# Adicionando elementos na lista em uma posição específica:
lanche.insert(0, 'cachorro-quente')
print(lanche)

# Apagando elementos:
del lanche[3] # Repare que aqui não temos um método e sim um comando, logo usanos [].
print(lanche)
lanche.pop(3) # Repare que aqui usamos um método e usamos () em todo e qualquer método. Normalmente o método pop é usado para excluir o último elemento, mas você pode escolher a posição do elemento a ser deletado.
print(lanche)
lanche.remove('suco') #Eu não vou indicar o índice que eu quero excluir e sim o valor. 
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')
    
valores = list(range(2, 11)) # O range ele cria uma estrutura já organizada.  
print(valores)

valores = [8, 9, 5, 1, 6, 3]
valores.sort() # Aqui eu apenas organizo minha lista sem necessariamente imprimí-la.
print(valores.sort()) # Aqui eu tenho o método sort. Quando você faz print(valores.sort()), está imprimindo o resultado da chamada do método sort(), que é None, pois o método sort() não retorna nada explicitamente. 
print(sorted(valores)) # E aqui tenho a função embutida do python

# Se eu quiser ordenar de forma inversa basta usar o método reverse:
valores.sort(reverse=True)
print(valores)

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(0, 2) # Na posição 0 eu quero adicionar o número 4.
num.pop(2)
num.remove(2) #Ele só remove o primeiro elemento
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valor = [] # Também poderia usar list() para criar uma lista.
valor.append(5)
valor.append(9)
valor.append(4)
for v in valor:
    print(f'{v}...', end = ' ')

for pos, v in enumerate(valor):
    print(f'\nNa posição {pos} o valor é {v}.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos, v in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {v}!')
print('Cheguei no final da lista.')

a = [2, 3, 4, 7]
b = a # Se eu quisesse criar uma cópia faria b=a[:]. Nesse caso b não tem ligação nenhuma com a. Logo, se eu quiser mudar algum elemento de b, sem alterar a, tenho que primeiro fazer uma cópia de a. 
b[2] = 9 # Aqui estou fazendo uma ligação de uma lista na outra. Ou seja, tudo que mudar em b mudará em a.
print(a)
print(b)
