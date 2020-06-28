from time import sleep
print('{:=^40}'.format('\033[4;36m TABUADA \033[m'))
n = int(input('Digite tabuada: '))
print('A tabuada de {} é: '.format(n))
for c in range (0, 11):
    print('{} x {:2} = {:2}'.format(n, c, n * c))
    sleep(1)
print(' Fim')