# ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

for c in range(1,10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

# SE EU NÃO SEI O LIMITE:
for c in range(1,5):
    n = int(input('Digite um valor: '))
print("FIM")

n = 1
while n != 0: # Isso é chamado de flag(condição de parada)
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    if n != 0:
        n = int(input('Digite um número: '))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
    