from os import system
system('cls')
maior = 0 
menor = 500
for i in range(5):
    peso = float(input(f'Digite o peso da {i+1}° pessoa: '))
    if (peso > maior):
        maior = peso
    elif(peso < menor):
        menor = peso
print(f'O maior peso foi {maior} e o menor foi {menor}')