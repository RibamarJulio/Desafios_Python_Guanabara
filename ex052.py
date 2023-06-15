from os import system
from math import sqrt, floor
system('cls')

n = int(input('Digite um número: '))

if (n % int(n**1/2) == 0 and n != 3 and n != 2):
    print(f'Número {n} NÃO é Primo ')
else:
    print(f'Número {n} É primo')