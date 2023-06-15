from os import system
system('cls')

velocidade = float(input('Digite sua velocidade: '))
if velocidade > 80:
    multa = (7 * ((velocidade - 80) // 1))
    print('Você foi multado...')
    print(f'Sua multa foi de R$ {multa:.2f}')
else:
    print('Parabéns. Segurança em primeiro lugar...')