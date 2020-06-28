d = float(input('\033[1;34m Qual a distância da viagem em km?\033[m '))
if d <= 200:
    print('O valor da passagem é R$ \033[4;32m{:.2f}\033[m'.format( d * 0.50 ))
else:
    print('O valor da sua passagem é R$ \033[4;32m{:.2f}\033[m'.format( d * 0.45))