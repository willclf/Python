from random import randint
from time import sleep
lista = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
#print(lista[pc])
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
player = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print('╔══════════════════════╗')
print('Computador jogou {}'.format(lista[pc]))
print(' Jogador jogou {}'.format(lista[player]))
print('╚══════════════════════╝')
if pc == 0:
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('PARABÉNS! Você venceu')
    elif player == 2:
        print('Computador GANHOU! Tente novamente.')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1:
    if player == 0:
        print('Computador GANHOU! Tente novamente.')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('PARABÉNS! Você venceu')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:
    if player == 0:
        print('PARABÉNS! Você venceu')
    elif player == 1:
        print('Computador GANHOU! Tente novamente.')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')


