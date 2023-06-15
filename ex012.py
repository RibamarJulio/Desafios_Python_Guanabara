from os import system
system('cls')
preco=float(input('Digite o preço do produto: '))
desconto=preco*0.05
print(f'O preço do produto {preco} com desconto de {desconto}, fica {preco-desconto}')