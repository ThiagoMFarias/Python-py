# Fatiamento:

frase = 'Curso em Vídeo Python'

print(frase[9]) # Só imprimie o índide (caractere).
print(frase[9:13]) # O 13 não entra. O último carater não entra na contagem. É sempre um a menos no final.
print(frase[9:65]) # Vai até o final mesmo que passe do número do índice.
print(frase[9:21:2]) # Vai do 9 ao 21 de dois em dois.
print(frase[:5]) # Extrairá os primeiros cinco caracteres da string. Lembrando que o índice começa com 0.
print(frase[15:]) # Começa no 16º caractere e vai até o final da string.
print(frase[9::3]) # Começa do índide 9 e vai até o final pulando de 3 em 3.

# Análise:
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) # Pedindo pra contar já com fatiamento do índice 0 até o 13.
print(frase.find('Terminator')) # Quando eu procuro uma string e ela não existe, é retornado o valor '-1'.
print('curso' in frase) # Verifica se a string "curso" está na variável "frase". 

# Transformação:
frase.replace('Curso', 'Android') # Nesse caso eu não mandei salvar o resultado e se eu mandar imprimir, ele imprimirá a frase original, e não com esse replace. Agora se eu atibuir a uma nova variável, aí dá certo!
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # Só a primeira letra em maiúscula
print(frase.title()) # Cada início de palavra ele põe em maiúscula
print(frase.strip()) # Remove todos os espaços no início e no fim da string. 
print(frase.rstrip()) # Remove só os espaços da direita.
print(frase.lstrip()) # Remove só os espaços da esquerda.

# Divisão:
print(frase.split()) # Transforma cada palavra em um novo índice: 'Curso' = 0, 'em' = 1, 'Vídeo' = 2, 'Python' = 3
dividido = frase.split()
print(dividido[0])

# Junção:
print('-'.join(frase))

# Teste
print(frase.lower().find('curso'))

#salvando um replace
frase=frase.replace('com', 'através')
print(frase)