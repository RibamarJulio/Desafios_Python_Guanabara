from os import system
system('cls')
print('Vamos ver se essa fazer é uma Palídromo? ')
frase = input('Digite uma frase: ').upper().strip()
frase = frase.split()
frase = ''.join(frase)
if (frase == frase[::-1]):
    print('Essa frase é um Palídromo')
    print(f'frase {frase} e inverso {frase[::-1]}')
else:
    print('Essa frase não é um Palídromo')