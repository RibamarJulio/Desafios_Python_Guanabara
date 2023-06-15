from os import system
system('cls')

p1 = int(input('Digite o primeiro comprimento: ')) # solicitar primeira medida
p2 = int(input('Digite o segundo comprimento: ')) # solicitar a segunda medida 
p3 = int(input('Digite o terceiro comprimento: ')) # solicitar a terceira medida

if(((p2 - p3) < p1 < (p2 + p3)) and ((p1 - p3) < p2 < (p1 + p2)) and ((p2 - p1) < p3 < (p1 + p2))): #verificar ser os valores formam um triângulo
    print(f'Esse valores formaram um triângulo: {p1}, {p2}, {p3}')
else:
    print(f'Esse valores não formaram um triangulo: {p1}, {p2}, {p3}')