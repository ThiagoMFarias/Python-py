'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    resp = ''
    if 0 <= num <= 20:
        print(f'Você digitou o número {números[num]}.')
        while True:
            resp = input('Quer continuar? [S/N]').strip().upper()[0]
            if resp == 'S' or 'N':  #Ainda não consegui resolver esse bug sem ser por função. 
                break
            else:
                print('Digite uma resposta válida.')
    if resp == 'N':
        break
    if num < 0 or num >20:
        print('Tente novamente. Digite um número válido!')
