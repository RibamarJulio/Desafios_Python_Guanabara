from os import system
system('cls')
from random import randint
sorte = randint(0,10)
adivinha = 11
cont = 0
while adivinha != sorte:
    adivinha = int(input('Digite um número entre 0 a 10: '))
    cont += 1
print(f'Você acertouuuu, só precisou de {cont} tentativas.')

