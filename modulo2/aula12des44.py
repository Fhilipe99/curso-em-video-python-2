valorProduto = float(input('Digite o valor do produto: '))
print('1 - A vista (desconto de 10%)')
print('2 - A vista no cartão (desconto de 5%)')
print('3 - Parcelado 2x no cartão')
print('4 - parcelado em 3x ou mais no cartão (com juros de 20%)')
pagamento = int(input('Digite a condição de pagamento: '))

if pagamento == 1:
    valorProduto = valorProduto - (valorProduto * 0.10)
    print(f'Com o desconto de 10% o valor vai sair {valorProduto} ')
elif pagamento == 2:
    valorProduto = valorProduto - (valorProduto * 0.05)
    print(f'Com o desconto de 5% o valor vai sair {valorProduto} ')
elif pagamento == 3:
    print(f'O produto sem desconto vai sair {valorProduto} ')
elif pagamento == 4:
    valorProduto = valorProduto * 1.20
    print(f'O valor do produto com os juros vai sair {valorProduto} ')
else:
    print('Opção invalida')