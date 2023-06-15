from os import system
system('cls')
a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('É alfaberto: ', a.isalpha())
print('É numérico: ', a.isnumeric())
print('É espaço: ', a.isspace())
print('É maiusculo: ', a.isupper())
print('É minusculo: ', a.islower())
