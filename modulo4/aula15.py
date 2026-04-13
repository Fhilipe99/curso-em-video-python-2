numSecreto = 7

while True:
    tentativa = int(input('Adivinhe o numero secreto: '))

    if tentativa == numSecreto:
        print('Parabens! Você acertou!')
        break

    print('Você errou, tente novamente!')

print('Fim do jogo!')