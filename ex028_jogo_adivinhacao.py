from random import randint
from time import sleep
c = randint(0,5)
print('Jogo da Adivinhação')
print('Tente me vencer...')
n = int(input('Em que numero eu pensei entre 0 e 5? '))
print('Somente numero entre 0 e 5'if n > 5 or n < 0 else 'PROCESSANDO...')
sleep(3)
if n == c:
    print('Parabéns, você venceu!!!')
else:
    print('Você perdeu, eu pensei no numero {} e não {}'.format(c,n))




