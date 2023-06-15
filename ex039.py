from os import system
system('cls')
from datetime import date, datetime
data_atual = int(date.today().year)
ano=int(input('Digite sua ano de seu nascimento: '))
idade = data_atual - ano
if(idade > 0 and idade < 18):
    print(f'Você tem {idade} anos, e falta {18-idade} anos para se alistar.')
elif(idade == 18):
    print(f'Você tem {idade} anos, e está na idade de se alistar.')
elif(idade > 18 and ano < data_atual):
    print(f'Você tem {idade} anos, e já deveria ter se alistado a {idade - 18} anos atrás.')
else:
    print('Ano informado inválido ')
