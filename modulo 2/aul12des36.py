valorCasa = float(input('Qual o valor da casa?: R$'))
salario = float(input('Qual o seu salario?: R$ ' ))
anos = int(input('Quantos anos de financiamento?: '))

prestacao = valorCasa / (anos * 12)

valor = salario * 0.30
if prestacao <= valor:
    print(f'A prestação por mês ficou em {prestacao:.2f}\nO limite permitido é {valor:.2f}\nVamos liberar o emprestimo!')
else:
    print(f'A prestação por mês ficou {prestacao:.2f}\nO limite permitido é {valor:.2f}\nNão iremos liberar o emprestimo!')
