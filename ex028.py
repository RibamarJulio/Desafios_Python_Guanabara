from os import system
system('cls')
from random import randint
n = randint(0,5)
n1 = int(input('Digite um número de 0 a 5: '))

if (n1 == n ):
    print('Você é demais...')
else:
    print('Não foi dessa vez, mas não desista...')
print(f'Número que você escolheu foi {n1} o número correto é {n}')