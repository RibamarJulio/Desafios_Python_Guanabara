from os import system
system('cls')

nome = input('Digite o seu nome: ').strip().upper()
existe = ('SILVA' in nome)

print('Seu nome tem Silva: {}'.format(existe))
print('Seu nome tem Silva: {}'. format(nome.count('SILVA')))


# if existe:
#     print(f"Existe Silva em {nome}")
# else:
#     print(f'Não existe Silva em {nome}')