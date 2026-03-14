
numero = int(input('Digite um numero: '))

for c in range(2 , numero):
    if numero % c == 0:
        primo = False
        print('O numero não é primo')
        break
else:
    primo = True
    print('O numero é primo')


