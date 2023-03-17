#esse eu não soube fazer pois as funções não estavam dando o calor correto. 
#tive que converter de radianos para graus. 
import math

angulo = float(input('Qual o ângulo que você quer calcular o seno, cosseno e tangente?\n'))
sen1 = math.radians(angulo)
seno = math.sin(sen1)
cos1 = math.radians(angulo)
cosseno = math.cos(cos1)
tan1 = math.radians(angulo)
tangente = math.tan(tan1)
print('O valor do seno é {}, do cosseno é {} e da tangente é {}.'.format(seno, cosseno, tangente))

#outra forma de fazer é:
import math

ângulo = int(input('Qual o ângulo você quer calcular o seno, cosseno e tangente?\n'))
sen = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))
print('O seno do ângulo {} é {:.2f}, o cosseno é {:.2f} e a tagente é {:.2f}'.format(ângulo, sen, cos, tan,))
