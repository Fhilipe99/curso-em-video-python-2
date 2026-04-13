primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termoAtual = primeiroTermo
contador = 0

while contador < 10:
    print(termoAtual)
    termoAtual += razao
    contador += 1