ent = input('Digite qualquer coisa: ')
print('O tipo primitivo dessa variável é {}'.format(type(ent)))
print('Só têm espaços? {}'.format(ent.isspace()))
print('É um número? {}'.format(ent.isnumeric()))
print('É alfabético? {}'.format(ent.isalpha()))
print('É alfanumérico? {}'.format(ent.isalnum()))
print('Está tudo em maiúsculaw {}'.formart(ent.isupper()))
print('Está em minúsculaw {}'.format(ent.islower()))
print('Está capitalizada? {}'.format(ent.istitle())) # Só com a primeira letras maiúscula