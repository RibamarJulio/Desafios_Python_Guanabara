from os import system
system('cls')

n1 = int(input('Digite seu primeiro número: '))
n2 = int(input('Digite seu segundo número: '))
incremento = 0 
if (n2 > n1):
    incremento =  n1
    n1 = n2 
    n2 = incremento
print(n1,n2)
n3 = int(input('Digite o terceiro número: '))
if (n3 > n1):
    incremento = n1 
    n1 =  n3
    n3 = n2 
    n2 = incremento
elif(n3 > n2):
    incremento = n2
    n2 = n3 
    n3 = incremento 
print(f'Maior número: {n1}\nIntermediário: {n2}\nMenor número: {n3}')