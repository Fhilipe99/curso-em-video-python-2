r1 = int(input('Digite o primeiro valor da reta: '))
r2 = int(input('Digite o segundo valor da reta: '))
r3 = int(input('Digite o terceiro valor da reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não é possível formar um triângulo')