from os import system
system('cls')
from time import sleep
from random import randint
from PIL import Image
print('Bora jogar jokenpô')
res = input('Sim OU Não? ').upper()
if(res == 'SIM'):
    opcao = randint(1, 3)
    print('Jóóóóó')
    sleep(1)
    print('quemmmm')
    sleep(1)
    print('póóóó')
    if(opcao == 1):
        print(' ___________')
        print('|  |  |  |  |')
        print('|___        |')
        print('|___|_______|')
    elif(opcao == 2):
        print('___       ___')
        print('\  \     /  /')
        print(' \  \   /  / ')
        print(' |   \ /  / ')
        print(' |__      | ')
        print(' |  |_____| ')
    elif(opcao == 3):
        print('     _   _   _   _')
        print('    | | | | | | | |')
        print('    | | | | | | | |')
        print('    |             |')
        print(' ___|             |')
        print('|_________________|') 
else:
    print('Seu(ua) chato(a)...')