while True:
    n = int(input('Digite um numero da tabuada (0 para encerrar): '))
    if n == 0:
        print('Parando o programa...')
        break
    print(f'A tabuada de {n} é: ')
    for multi in range(1, 11):
        resultado = n * multi
        print(f'{n} x {multi:2} = {resultado:3}')
    print()
