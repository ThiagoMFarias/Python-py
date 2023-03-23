import math

# Faça um programa que leia o cateto oposto e o cateto adjacente e calcule a hipotenusa

cat_op = float(input('Qual o cateto oposto do triângulo? '))
cat_adj = float(input('Qual o cateto adjacente do triângulo? '))
hipotenusa = math.hypot(cat_op, cat_adj)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

# outra forma de fazer:    
co = float(input('Qual o cateto oposto? '))
ca = float(input('qual o cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é gual a {}'.format(hi))
