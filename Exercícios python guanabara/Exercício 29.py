speed = int(input('Qual a velocidade do carro?'))
multa = (speed - 80) * 7
if speed > 80:
    print('Você foi multado por andar acima de {}km/h'.format(speed))
    print('Você irá pagar R$ {}'.format(multa))