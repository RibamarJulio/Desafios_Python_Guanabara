from os import system
system('cls')

peso = int(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)
if(imc > 0 and imc < 18.5):
    status = 'Abaixo do peso'
elif(imc > 18.5 and imc <= 25):
    status = 'Peso ideal'
elif(imc > 25 and imc <= 30):
    status = 'Sobrepeso'
elif(imc > 30 and imc <= 40):
    status = 'Obesidade'
elif(imc > 40):
    status = 'Obesidade Mórbida'
else: 
    status = 'Valor inválido'
print(f'Seu imc é {imc:.2f}\nStatus: {status}')
