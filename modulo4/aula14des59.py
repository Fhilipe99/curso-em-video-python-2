n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0

while opcao != 5:

    print('''MENU
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair''')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação de {n1} * {n2} = {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior numero entre {n1} e {n2} é {maior}')
        else:
            maior = n2
            print(f'O maior numero entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        pass
    else:
        print('Opção invalida, escolha uma das opções validas')
else:
    print('Saindo do programa')



