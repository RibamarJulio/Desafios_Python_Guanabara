from os import system
system('cls')
from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for i in range(7):
    ano = int(input(f'Digite o ano da {i+1}° pessoa: '))
    idade = ano_atual - ano
    if (idade < 20):
        menor += 1
    else:
        maior += 1
print(f'De todas as idades informadas, {menor} são de menor e {maior} são de maior.')