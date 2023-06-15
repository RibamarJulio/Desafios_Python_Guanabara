from os import system
system('cls')
salario=float(input('Digite seu salário: '))
aumento=salario*1.15
print(f'Seu salário de {salario} com aumento de 15% vai para {aumento:.2f}')