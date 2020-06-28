print('\033[1;36m-=-\033[m'*20)
print('\033[1;34m Aumento de Salário \033[m')
print('\033[1;36m-=-\033[m'*20)
atual = float(input('\033[1;31;3mQual seu sálario? R$ \033[m'))
if atual <= 1250:
    novo = atual + (atual * 15 / 100)
else:
    novo = atual + (atual * 10 / 100)
print ('\033[4;37mSeu salário com aumento será de R$ \033[1;34m{:.2f}\033[m'.format(novo))