from os import system
system('cls')
numero = int(input('Escolha qualquer número: '))
opcao = int(input('Deseja converter para 1-binário, 2-Hexadecimal ou 3-octal: '))
resultado_final=''
if(opcao == 1):
    print(format(numero, 'b'))
elif(opcao == 2):
    print(format(numero, 'x'))
elif(opcao == 3):
    print(format(numero, 'o'))
else:
    print('Nenhuma opção válida...')
