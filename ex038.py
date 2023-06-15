from os import system 
system ('cls')

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite o segundo número qualquer: '))

if(n1 > n2):
    print(f'O primeiro número {n1}, é maior que o segundo {n2}')
elif(n2 > n1):
    print(f'O segundo número {n2} é maior que o primeiro {n1}')
else:
    print(f'O primeiro {n1} e segundo {n2} números são iguais')
    