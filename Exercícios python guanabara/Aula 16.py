# Variáveis compostas (tuplas, listas e dicionários)
# Tuplas são boas para guardar elementos

tupla = 'hamburguer', 'cerveja', 'pizza', 'pudim' # SÃO IMUTÁVEIS!!!!!!!!!!!

print(tupla[1])
print(tupla[0:2]) # lembre-se que nesse fatiamento não contamos com o último índice.
print(tupla[1:]) # lembre-se que vai de 1 até o último
print(tupla[-1]) # É o último elemento. Sempre de trás pra frente! O hamburguer ou é índice -4 ou índice 0.
print(len(tupla))
for i in tupla: #(A)
    print(i)
""" tupla[1] = 'arroz'
print(tupla[1]) """

for cont in range(0, len(tupla)):
    print(cont)
for cont in range(0, len(tupla)):
    print(tupla)
for cont in range (0, len(tupla)): # É igual a letra A. exibe o mesmo resultado. 
    print(tupla[cont])
for cont in range (0, len(tupla)):
    print(f'Vou comer {tupla[cont]} na posição {cont}.')
for pos, cont in enumerate(tupla):
    print(f'Eu vou comer {tupla} na posição {pos}.')

print(sorted(tupla)) # Aqui a resposta vem em forma de lista!!!
print(tupla)

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2, 4)) # a partir da posição 4. Eu chamo isso de deslocamento

pessoa = ('Gustavo', 39, 'M', 72.00) # posso ter todo tipo de dado, string, int, float, etc.
del(pessoa)
print(pessoa) # como eu apaguei a variável ela não existe mais. 