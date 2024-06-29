'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''

from random import randint

num = int(input('Quantos jogos você quer fazer? '))
jogo_temp = []
jogo = []

for i in range (num):
    for c in range(6):
        while len(jogo_temp) < 6:
            jogos = randint(1, 60)
            if jogos not in jogo_temp:
                jogo_temp.append(jogos)
    jogo_temp.sort()
    jogo.append(jogo_temp[:])
    jogo_temp.clear()
print(sorted(jogo))

# Resolução do GPT:

""" from random import sample

num = int(input('Quantos jogos você quer fazer? '))

jogo = []

for _ in range(num):
    novo_jogo = sorted(sample(range(1, 61), 6))  # Usando sample() para gerar 6 números únicos
    jogo.append(novo_jogo)

print(jogo) """


