from os import system
system('cls')
numero = int(input('Digite um número de 0 a 9999: '))
# tam = len(numero)
# if tam == 3:
#     numero = '0' + numero
# elif tam ==2:
#     numero = '00' + numero
# elif tam == 1:
#     numero = '000' + numero
u = numero // 1 % 10
d = numero // 10 % 10 
c = numero // 100 % 10
m = numero // 1000 % 10 

print(f'Unidade: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')

