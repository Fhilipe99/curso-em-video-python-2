import datetime
print('Verificador de Idade')
dataAtual = datetime.date.today().year
adulto = 0
menores = 0

for c in range(1,8):
    ano = int(input(f'Pessoa {c}, digite seu ano de nascimento: '))
    idade = dataAtual - ano

    if idade > 18:
        adulto = adulto + 1
    else:
        menores = menores + 1

print(f'Maiores de idade: {adulto}')
print(f'Menores de idade: {menores}')




