from os import system
system('cls')

valor_emprestimo = float(input('Qual o valor do empréstimo? '))
salario = float(input('Qual o valor do seu salário? '))
parcelas = int(input('Em quantos anos pretence pagar? '))

valor_por_parcela = valor_emprestimo / (parcelas * 12)
if (valor_por_parcela <= (salario * 0.3)):
    print(f'Empréstimo aprovado\nValor das parcela: {valor_por_parcela:.2f}')
else:
    print(f'Empréstimo negado\nParcelas incompatível com salário {valor_por_parcela:.2f}')