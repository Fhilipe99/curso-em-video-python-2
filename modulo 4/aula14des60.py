fatorial = 1
resultado = 1
opcao = 0
while opcao != 2:
    print('''MENU
        [ 1 ] Descobrir fatorial
        [ 2 ] Sair''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
            fatorial = int(input('Digite um numero para descobrir o fatorial: '))
            numero = fatorial
            while fatorial != 1:
                resultado = resultado * fatorial
                fatorial = fatorial - 1
            print(f'O resultado do fatorial de {numero} é {resultado}')
    elif opcao == 2:
        pass
    else:
        print('Opção invalida')
else:
    print('Saindo do programa')






