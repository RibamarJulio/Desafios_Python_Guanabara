from os import system
system('cls')
nome = input('Digite seu nome completo: ').strip()
fracao = nome.split()
tam = len(''.join(fracao))
print(f'Maiusculo: {nome.upper()}')
print(f"Minusculo: {nome.lower()}")
print(f"Tamanho: {tam}")
print(f"Primeiro Nome: {len(fracao[0])}")