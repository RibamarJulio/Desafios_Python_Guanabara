from math import sqrt
from os import system
system('cls')
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente: '))
h=(co*co + ca*ca)
print(f'A hipotenusa é {sqrt(h):.2f}')