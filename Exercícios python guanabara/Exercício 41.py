'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER'''

import datetime

print('=-=-=-=-=-=-' * 5)
print('         Bem vindo(a) ao Cadastro de atletas da CNN')
print('=-=-=-=-=-=-' * 5)

ano_atual = datetime.date.today().year
ano_nasci = int(input('Insira agora o ano você nasceu: '))
idade = ano_atual - ano_nasci

if idade < 9:
    print('Sua categoria é MIRIM.')
elif 9 <= idade <14:
    print('Sua categoria é INFANTIL.')
elif 14 <= idade < 19:
    print('Sua categoria é JUNIOR.')
elif 19 <= idade < 20:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.') 
    