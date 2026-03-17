a = 0
b = 1
n = int(input('Digite um numero inteiro: '))
contador = 0
while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1
