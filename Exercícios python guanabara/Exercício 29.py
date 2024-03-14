# Escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite. 

speed = int(input('Qual a velocidade do carro?'))
multa = (speed - 80) * 7
if speed > 80:
    print('Você foi multado por andar acima de {}km/h'.format(speed))
    print('Você irá pagar R$ {}'.format(multa))
    