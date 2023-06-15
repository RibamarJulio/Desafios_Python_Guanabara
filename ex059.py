from os import system 
system('cls')

opcao = 0
while opcao != 5:
    v1 = float(input('Digite um valor qualquer: '))
    v2 = float(input('Digite um segundo valor qualquer: '))
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do programa')
    opcao = int(input('Qual: '))
    if (opcao == 1):
        print(f'{v1} + {v2} = {v1+v2}')
    elif (opcao == 2):
        print(f'{v1} x {v2} = {v1*v2}')
    elif (opcao == 3):
        if (v1 > v2):
            print(f'Maior é {v1}')
        else:
            print(f'Maior é {v2}')
    elif (opcao == 4):
        print('Bora de novo')
