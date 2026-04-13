soma = 0
idadeMaior = 0
nomeVelho = ''
totalMulheres = 0

for c in range(1,5):
    nome = input(f'Pessoa {c}: ').strip().upper()
    idade = int(input(f'Idade {c}: '))
    sexo = input(f'Sexo {c}: ')

    soma = soma + idade

    if idade > idadeMaior and sexo == 'M':
        idadeMaior = idade
        nomeVelho = nome

    if idade < 20 and sexo == 'F':
        totalMulheres = totalMulheres + 1

media = soma / 4

print(f'A media de idade do grupo é: {media}')
print(f'O homem mais velho é {nomeVelho}, com {idadeMaior} anos')
print(f'A quantidade de mulheres com menos de 20 anos é: {totalMulheres}')


