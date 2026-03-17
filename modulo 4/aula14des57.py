sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido, digite novamente.')
if sexo == 'M':
    print('Sexo Masculino')
else:
    print('Sexo Feminino')
print('Fim')