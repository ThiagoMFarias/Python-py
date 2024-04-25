# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))

suc = n1 + 1
ant = n1 - 1

print('O sucessor de {} é {}, e seu antecessor é {}'.format(n1, suc, ant))

# print('O sucessor de {} é {}, e seu antecessor é {}'.format(n1, (n1+1), (n1-1)))
# quanto menos variáveis eu usar no meu programa, mais memória eu economizo!!!
