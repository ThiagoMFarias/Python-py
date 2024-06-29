ent = input('Digite qualquer coisa: ')
print('O tipo primitivo dessa variável é {}'.format(type(ent)))
print('Só têm espaços? {}'.format(ent.isspace()))
print('É um número? {}'.format(ent.isnumeric()))
print('É alfabético? {}'.format(ent.isalpha()))
print('É alfanumérico? {}'.format(ent.isalnum()))
print('Está tudo em maiúscula? {}'.format(ent.isupper()))
print('Está em minúscula? {}'.format(ent.islower()))
print('Está capitalizada? {}'.format(ent.istitle())) # Só com a primeira letras maiúscula
