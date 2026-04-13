n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        print('Finalizando...')
        break
    s += n
    c += 1
print(f'A quantidade de numeros digitados foi {c}, e a soma deles foi {s}! ')