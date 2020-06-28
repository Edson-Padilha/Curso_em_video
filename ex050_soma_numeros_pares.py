print('\033[4;36m{:=^40}\033[m'.format(' SOMA DE NUMEROS PARES '))
cont = 0
soma = 0
for c in range(0, 6):
    n = int(input('Digite numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos numeros digitados é: {}'.format(soma))