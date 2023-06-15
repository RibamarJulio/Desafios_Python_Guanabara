from os import system
system('cls')
soma = 0
for i in range(6):
    n = int(input(f'Digite o {i+1}° número: '))
    if (n % 2 == 0):
        soma += n
print(f'O valor somado de todos os número pares digitado é {soma}')