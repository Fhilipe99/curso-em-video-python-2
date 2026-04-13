n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

resultado = (n1 + n2) / 2

print(f'A nota final foi {resultado}, você está: ')

if resultado < 5.0:
    print('Reprovado')
elif 5.0 <= resultado <= 5.9:
    print('Recuperação')
else:
    print('Aprovado')