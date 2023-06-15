from os import system
system('cls')
valor_total = float(input('Valor total: '))
print('''[1] À VISTA: Dinheiro/Cheque
[2] À VISTA CARTÃO
[3] 2 x CARTÃO 
[4] 3/+ x CARTÃO''')
opcao = int(input('Qual opção: '))
if(opcao == 1):
    desconto = valor_total * 0.1
    apagar = valor_total - desconto
elif(opcao == 2):
    desconto = valor_total * 0.05
    apagar = valor_total - desconto
elif(opcao == 3):
    desconto = 0
    apagar = valor_total - desconto
elif(opcao == 4):
    desconto = valor_total * .2
    apagar = valor_total + desconto
else:
    print('Opção invalida...')
    desconto = 0
    apagar = 0
print(f'Valor Total: {valor_total:.2f}\nValor do Desconto: {desconto:.2f}\nValor a pagar: {apagar:.2f} ')