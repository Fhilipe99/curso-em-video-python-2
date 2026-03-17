num = 0
soma = 0
media = 0
opcao = ''
contador = 0
maior = float('-inf')
menor = float('inf')
while opcao != 'N':
    contador += 1
    num = int(input('Digite um numero: '))
    soma += num
    media = soma / contador
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao:
        opcao = opcao[0]
    if opcao not in ['S', 'N']:  # verifica se é válido
        print('Digite S ou N')
        opcao = 'S'
print(f'O total de numeros foi {contador}, a média desses numeros foi de {round(media,2)}, o maior numero foi {maior}, e o menor numero foi {menor}')
