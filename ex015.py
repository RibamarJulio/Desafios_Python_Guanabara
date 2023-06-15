from os import system
system('cls')
dia = int(input("Quantos dias alugado: "))
km = float(input("Quantos kilometro percorrido: "))
valor = (dia*60)+(km*0.15)
print('O valor a pagar é {}'.format(valor))