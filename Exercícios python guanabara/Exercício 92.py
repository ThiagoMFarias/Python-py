"Crie um programa que leia o nome, o ano de nascimento e a carteira de trabalho e cadastre-os(com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."
from datetime import datetime

dados = {'Nome': str(input('- Nome: ').title()),
         'Nº Carteira de Trabalho': int(input('- Nº Carteira de Trabalho: ')),
        }
nasc = int(input('- Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc

if dados['Nº Carteira de Trabalho'] != 0:
    dados['Ano de Contratação'] = int(input('- Ano de contratação: '))
    dados['Salário'] = float(input('- Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de Contratação'] + 35) - datetime.now().year)
print('-=' * 30)

for k, v in dados.items():
    print(f'- {k} tem valor {v}.')
