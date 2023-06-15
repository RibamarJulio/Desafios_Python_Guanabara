from os import system
from random import randrange
system('cls')
nomes=[]
ordem=[]
for x in range(4):
    nome=input(f'Digite o {x+1}° nome: ')
    nomes.append(nome)
    while True:
        sorte=randrange(0,4)
        if sorte not in ordem:
            ordem.append(sorte)
            break
system('cls')
for o in (ordem):
    print(f'Ordem de apresentação é {nomes[o]}')
            
    
    