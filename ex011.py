from os import system
system('cls')
altura=float(input('Qual a altura: '))
largura=float(input('Qual o largura: '))
metros=altura*largura
l_tinta=metros/2
print(f'Para pintar uma áres de {metros}, é preciso {l_tinta} litros de tinta')