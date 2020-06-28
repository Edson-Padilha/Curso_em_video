
print('-' * 70)
atual = float(input('Qual seu salário atual? R$ '))
novo = atual + (atual * 15 / 100)
print('Você ganhava R$ {:.2f}, com aumento de 15% vai ganhar R$ {:.2f}'.format(atual, novo))
print('-' * 70)