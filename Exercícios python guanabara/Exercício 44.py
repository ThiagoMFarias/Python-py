'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro /cheque: 10% de desconto;
- à vista no cartão: 5% de desconto;
- em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20.'''

print('---------------------------------------')
print('TORRA-TORRA DE PREÇOS NO VAREJÃO THIAGO')
print('---------------------------------------')
prod = float(input('Qual o valor do produto escolhido: R$ '))
forma_pag = int(input('''Qual a forma de pagamento:
[1] À vista 
[2] À no cartão 
[3] 2X no cartão 
[4] 3X ou mais no cartão \n'''))

if forma_pag == 1:
    desconto = prod - (prod * 0.1)
    print('Você terá 10% de desconto. O valor final da compra ficará R$ {:.2f}'.format (desconto))
elif forma_pag == 2:
    desconto = prod - (prod * 0.05)
    print('Você terá 5% de desconto. O valor final da compra ficará R$ {:.2f}'.format (desconto))
elif forma_pag == 3:
    desconto = prod - (prod * 0.05)
    print('Você não terá desconto. O valor final da compra ficará R$ {:.2f}'.format (prod))
elif forma_pag == 4:
    juros = prod + (prod * 0.2)
    print('Você terá um acréscimo na sua conta de 20%. O valor final da compra ficará R$ {:.2f}'.format (juros))
else:
    print('Digite a opção correta!')
    