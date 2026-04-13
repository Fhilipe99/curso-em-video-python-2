import random

print('Preparado para jogar pedra, papel e tesoura?')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
jogadaUsuario = int(input('Escolha sua jogada: '))

jogadaPC = random.randint(1, 3)
print(jogadaPC)
if jogadaUsuario == jogadaPC:
    print('Anulado')
elif (jogadaUsuario == 1 and jogadaPC == 3) or (jogadaPC == 1 and jogadaUsuario == 3):
    print('Pedra venceu!')
elif (jogadaUsuario == 2 and jogadaPC == 1) or (jogadaPC == 2 and jogadaUsuario == 1):
    print('Papel venceu!')
elif (jogadaUsuario == 3 and jogadaPC == 2) or (jogadaPC == 3 and jogadaUsuario == 2):
    print('Tesoura venceu!')

