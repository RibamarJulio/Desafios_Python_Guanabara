from os import system
system('cls')
nome_mais = ''
cont_mulher = 0
soma = 0
idade_maior = 0
for i in range(4):
    print(f'{i + 1}° Candidato:')
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo H ou M: ').upper()
    soma += idade
    if (idade > idade_maior and sexo == 'H'):
        nome_mais = nome
    if(sexo == 'M' and idade < 20):
        cont_mulher += 1
    system('cls')
print(f'A média de idade: {soma/4}')
print(f'O nome do homem mais velho: {nome_mais}')
print(f'Mulheres com menos de 20 anos: {cont_mulher}')
    
    