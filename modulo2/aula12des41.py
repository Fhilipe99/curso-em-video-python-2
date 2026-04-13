import datetime

ano = datetime.date.today().year
nascimento = int(input('Ano de nascimento: '))

categoria = ano - nascimento

if categoria <= 9:
    print('Mirim')
elif 10 <= categoria <= 14:
    print('Infantil')
elif 15 <= categoria <= 19:
    print('Junior')
elif 20 <= categoria <= 24:
    print('Senior')
else:
    print('Master')
