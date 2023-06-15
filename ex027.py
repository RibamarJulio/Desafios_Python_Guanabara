from os import system 
system('cls')

nome = input('Digite um nome completo: ').strip()

divisao = nome.split()
print(f'Primeiro nome: {divisao[0]}')
print(f'Último nome: {divisao[len(divisao)-1]}')