from os import system 
system('cls')
resp = 'SIM'
while resp == 'SIM':
    sexo = input('Selecione uma sexo M / F: ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        resp = 'NÃO'
print(f'O sexo escolhido foi {sexo}')
