from random import randint
from time import sleep
print('\033[1;35m-=\033[m'*20)
print(' '*12,'\033[4;35m Jokempô \033[m')
print('''Opções:
[0] Papel
[1] Pedra
[2] Tesoura''')
lista = ('Papel', 'Pedra', 'Tesoura')
opcao = int(input('Qual sua jogada: '))
if opcao != 0 and opcao !=1 and opcao !=2:
    print('\033[4;36mOpção incorreta\033[m')
print('\033[1;32mJO\033[m')
sleep(1)
print('\033[1;33mKEN\033[m')
sleep(1)
print('\033[1;34mPO!!!\033[m')
sleep(1)
computador = randint (0,2)
print('Você escolheu a opção: {} e o computador: {}'.format(lista [opcao],(lista[computador])))
if opcao == 0 and computador == 1 or opcao == 1 and computador == 2 or opcao == 2 and computador == 0:
    print('\033[4;35mParabéns, você ganhou do computador!!!\033[m')
elif opcao == computador:
    print('\033[4;36mEmpate\033[m')
else:
    print('\033[4;36mO computador ganhou!\033[m')


