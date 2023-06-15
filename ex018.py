from os import system
from math import sin,cos,tan, radians
system('cls')
angulo=float(input('Digite um ângulo: '))
angulo= radians(angulo)
print(f'Seno do ângulo é: {sin(angulo):.2f} \nCosseno do ângulo é: {cos(angulo):.2f}\nTangente do ângulo é: {tan(angulo):.2f}')
