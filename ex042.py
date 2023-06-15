from os import system
system('cls')

c1 = int(input('Digite o primeiro valor: '))
c2 = int(input('Digite o segundo valor: '))
c3 = int(input('Digite o terceiro valor: '))

if(c1 < c2 + c3 and c2 < c3 + c1 and c3 < c1 + c2):
    if (c1 == c2 == c3):
        classificacao = 'Equilátero'
    elif(c1 != c2 != c3):
        classificacao = 'Escaleno'
    elif(c1 != c2 == c3 or c2 != c1 == c3 or c3 != c2 == c1):
        classificacao = 'Isósceles'
    print(f'Classificação do triângulo: {classificacao}')
else: 
    print('Não é um triângulo')
