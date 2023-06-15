from os import system
system('cls')

print('Todos os números impares que são multiplos de 3: ')
for c in range(0, 501):
    if (c % 2 != 0 and c / 3):
        print(c, end=', ')