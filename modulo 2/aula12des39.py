import datetime

data = datetime.date.today().year
nascimento = int(input('Em que ano você nasceu?:  '))

idade = data - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {data}')
if idade < 18:
    print(f'Você ainda vai se alistar no exercito, faltam {18 - idade} anos!')
elif idade == 18:
    print('Esta na hora de se alistar!')
else:
    print(f'Você ja passou do tempo do alistamento, passou {idade - 18} anos.')