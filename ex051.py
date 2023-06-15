from os import system
system('cls')

print('Vamos trabalhar com PROGRESSÃO ARITMÉTICA')
termo = int(input('Digite o TERMO: '))
razao = int(input('Digite a RAZÃO: '))
cont = 0
for i in range(10):
    cont += 1
    print(f'a{cont} {termo} = {termo} + {razao}')
    termo += razao