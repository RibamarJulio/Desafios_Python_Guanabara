from os import system
from time import sleep
system('cls')

bora = input('Bora iniciar a contagem para os fogos? SIM/NÃO ').upper().strip()
if (bora == 'SIM'):
    for c in range(10,-1,-1):
        print(c)
        sleep(1)
    print()
    print(' ********')
    print('**********')
    print(' ********')