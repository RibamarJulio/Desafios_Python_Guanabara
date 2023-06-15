from os import system
system('cls')

cidade = input('Digite o nome de uma cidade: ').strip()

print(cidade[:5].upper() == 'SANTO' )


# if  cidade.find('SANTO') == 0 :
#     print('A cidade: {} começa com Santo'.format(cidade))