from os import system
system('cls')

frase = input('Digite qualquer frase: ').strip()

print('Quantidade de a : {} '.format(frase.lower().count('a')))
print('Primeira vez: {}'.format(frase.find('a')+1))
print('Ultima vez: {}'.format(frase.rfind('a')+1))
