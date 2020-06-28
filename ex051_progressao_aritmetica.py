print('\033[1;34m{:=^40}\033[m'.format(' PROGRESSÃO ARITMÉTICA '))
n1 = int(input('Digite um numero: '))
r = int(input('Qual é a razão: '))
décimo = n1 + (10 - 1) * r
if r > 0:
    print('Progressão crescente')
elif r < 0:
        print('Progressão descrescente')
elif r == 0:
        print('Progressão constante')
for c in range(n1, décimo + r, r):
       print('{}'.format(c), end= '->')
print('Acabou')













