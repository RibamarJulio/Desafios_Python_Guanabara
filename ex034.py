from os import system
system('cls')

salario = float(input('Digite o valor do seu salário: R$ '))
if (salario <= 1250.00):
    salario = salario * 1.15
else:
    salario = salario * 1.1
print(f'Seu salário é {salario:.2f}')