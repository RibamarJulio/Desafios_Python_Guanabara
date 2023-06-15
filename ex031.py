from os import system
system('cls')

distancia = float(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    valor = 0.5 * distancia
else:
    valor = 0.45 * distancia

print(f'Sua viagem de {distancia}Km sairá por R$ {valor:.2f}')