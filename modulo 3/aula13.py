i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

if p <= 0 or f <= 0:
    print('Numero invalido, digite um numero maior que 0 no Fim e/ou Passo!')
    exit()
for c in range(i, f+1, p):
    print(c)
print('FIM')
