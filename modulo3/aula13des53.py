palavra = input('Digite uma palavra: ').strip().lower()
palavra_limpa = palavra.replace(' ','')
invertida = palavra_limpa[::-1]

if invertida == palavra_limpa:
    print(f'A palavra "{palavra}" é palindromo')
else:
    print(f'A palavra "{palavra}" não é palindromo')

