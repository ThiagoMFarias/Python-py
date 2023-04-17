nome = str(input('Qual é o seu nome?')).capitalize()

if nome == 'Thiago':
    print('Que nome lindo você tem!')
    print('Bom dia {}'.format(nome))
else:
    print('Seu nome é tão feio!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))

if m > 6.0:
    print('Parabéns, você passou!')
else:
    print('Vamos estudar mais garoto!')