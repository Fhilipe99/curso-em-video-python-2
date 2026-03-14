print('Verificação de maior e menor peso')

menor = float('inf')
maior = 0

for c in range(1,6):
    peso = float(input(f'Pessoa {c}, digite seu peso: '))

    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso é: {maior}')
print(f'O menor peso é: {menor}')


