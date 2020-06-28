n1 = int(input('Digite numero para calcular seu fatorial: '))
c = n1 +1
f = 1
for c in range(n1):
    print('{} '.format(c), end = '')
    print('x' if c > 1 else '=',end ='')