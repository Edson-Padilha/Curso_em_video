from random import randint
print('-=' * 20)
print(' Vamos jogar par ou impar')
print('-=' * 20)
computador = randint(1,10)
soma = True
while True:
    jogador = int(input('Digite um numero: '))
    opcao = str(input('Par ou Ímpar? P/I: ')).upper().strip()

    if opcao == 'P':
        soma = (jogador + computador) % 2 == 0
    if opcao == 'I':
        soma = (jogador + computador) % 3 == 1
    if soma == True:
     print(f'{computador} Parabéns você ganhou!!!')

    if soma == False:
     print('Você Perdeu!!!')
    break



