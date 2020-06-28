from time import sleep
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
print('Jogo da Adivinhação''\nSou seu computador...''\nAcabei de  pensar em um numero entre 0 e 10.''\nSerá que você consegue adivinhar qual foi?')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    print('Processando...')
    sleep(2)
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('\033[34mAcertou com {} tentativas. Parabéns!!!\033[m'.format(palpites))




