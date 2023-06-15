from random import randrange
from os import system
system('cls')
nomes=[]
for x in range(4):
    nome=input(f'Digite o {x+1}º nome: ')
    nomes.append(nome)
sorte=randrange(0,3)
print(f'Quem vai limpar o quadro é {nomes[sorte]}')

    