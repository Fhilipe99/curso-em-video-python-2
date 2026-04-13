contador_compras = 0
contador_1000 = 0
total = 0
menor = float('inf')

while True:
    nome_produto = input('Digite o nome do produto: ')
    valor = int(input('Digite o valor do produto: '))
    total += valor
    contador_compras += 1
    if valor > 1000:
        contador_1000 += 1
    if valor < menor:
        menor = valor
        nome_barato = nome_produto


    escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if escolha == 'N':
        print(f'Produtos custando mais de 1000: {contador_1000}')
        print(f'O total da compra foi R$ {total}')
        print(f'O produto mais barato foi o {nome_barato} de valor {menor}')
        break
