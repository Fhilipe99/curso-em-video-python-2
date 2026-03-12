number = int(input('Escreva um numero inteiro: '))
escolha = int(input('Você quer conversão para binario, octal, hexadecimal ou todas? Escolha 1, 2, 3 ou 4: '))

if escolha == 1:
    resultado = bin(number) [2:]
    print(f'O numero {number} em binario é {resultado}')
elif escolha == 2:
    resultado = oct(number) [2:]
    print(f'O numero {number} em octal é {resultado}')
elif escolha == 3:
    resultado = hex(number) [2:]
    print(f'O numero {number} em hexadecimal é {resultado} ')
elif escolha == 4:
    resultado = bin(number)[2:]
    resultado2 = oct(number)[2:]
    resultado3 = hex(number)[2:]
    print(f'O numero {number} em binario é {resultado}, em octal é {resultado2} e em hexadecimal é {resultado3} ')
else:
    print('Opção invalida')

