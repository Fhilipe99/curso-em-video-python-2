primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termoAtual = primeiroTermo
contador = 0
adicao = 0
while contador < 10:
    print(termoAtual)
    termoAtual += razao
    contador += 1

adicao = int(input('Digite quantos tempos mais você quer ver (0 para sair): '))

while adicao != 0:
    contador = 0
    while contador < adicao:
        print(termoAtual)
        termoAtual += razao
        contador += 1
    adicao = int(input('Digite quantos tempos mais você quer ver (0 para sair): '))
else:
    print('Encerrando o programa')