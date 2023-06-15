from os import system
system('cls')
celsius = float(input('Qual a temperatura em °Celsius: '))
fahrenheit = ((celsius * 9) / 5) + 32
print('A temperatura em {}°C é {}°F'.format(celsius,fahrenheit)) 