# Fatiamento:

frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:13]) # O 13 não entra.
print(frase[9:65])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise:
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('Terminator')) # Quando eu procuro uma string e ela não existe, é retornado o valor '-1'.
print('curso' in frase)

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
print('-'.join(frase))

# Teste

print(frase.lower().find('curso'))
