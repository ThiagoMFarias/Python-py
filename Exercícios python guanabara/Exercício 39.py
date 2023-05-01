'''Faça um programa que leia o ano de nasciento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou o tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime 

ano_atual = datetime.date.today().year
ano_nasci = int(input('Em que ano você nasceu? '))
alistamento = ano_atual - ano_nasci

if alistamento <= 17:
    print('Você ainda vai servir ao país nas Forças Armadas!')

if alistamento == 18:
    print('Parabéns.... chegou sua hora de se alistar!')

if alistamento > 18:
    print('===========' * 9)
    print('   Você já passou do tempo para se alistar! Se não fez sua obrigação, corra, ou vai pagar multa.')
    print('===========' * 9)