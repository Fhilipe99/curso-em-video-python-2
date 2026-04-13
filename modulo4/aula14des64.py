num = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        soma += num
print(f'A soma de todos os numeros ficou: {soma}')
