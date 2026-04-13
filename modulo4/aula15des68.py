import random

contador_rodadas = 0
while True:
    escolha = input('Par ou impar?: ').strip().lower()

    numero_jogador = int(input('Digite um numero: '))

    numero_computador = random.randint(0, 10)
    print(f'O computador escolheu: {numero_computador}')

    total = numero_computador + numero_jogador
    print(f'Soma: {numero_computador} + {numero_jogador} = {total}')
    if total % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    if escolha == resultado:
        contador_rodadas += 1
        print(f'Você ganhou essa rodada! Vitorias seguidas: {contador_rodadas}')
    else:
        print(f'Você perdeu! O resultado foi: {resultado}')
        print(f'Você venceu {contador_rodadas} vezes seguidas')
        break

    print()
