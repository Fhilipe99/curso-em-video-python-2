import random
num = None
adivinhacao = random.randint(1, 10)
tentativas = 0
while num != adivinhacao :
    tentativas += 1
    num = int(input('Digite um numero: '))
    if num > adivinhacao:
        print('Muito alto')
    else:
        print('Muito baixo')
if num == adivinhacao:
        print(f'Correto, o numero certo era {adivinhacao}, você levou {tentativas} tentativas')
print('Fim')