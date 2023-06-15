from os import system
system('cls')

tabuada = int(input('Digite um valor inteiro para ver sua tabuada: '))

for i in range(11):
    print(f'{i} x {tabuada} = {i*tabuada}')