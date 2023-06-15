from os import system
system('cls')
print('Todos os números pares no intervalo de 1 a 50:')
for c in range(1,51):
    if (c % 2 == 0):
        print(c, end=', ')
    