contador_maior18 = 0
contador_menor20 = 0
contador_homens = 0
idade = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (Apenas F/M): ').upper().strip()
    if idade > 18:
        contador_maior18 += 1
    if idade < 20 and sexo == 'F':
        contador_menor20 += 1
    if sexo == 'M':
        contador_homens += 1

    escolha = input('Deseja continuar? [S/N] ').upper()
    if escolha == 'N':
        print(f'A quantidade de pessoas maior que 18 é: {contador_maior18}')
        print(f'A quantidade de mulheres menor que 20 é: {contador_menor20}')
        print(f'O total de homens cadastrados é: {contador_homens}')
        break