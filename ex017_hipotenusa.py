from math import hypot
print('=' * 40)
o = float(input('Digite o cateto oposto: '))
a = float(input('Digite o cateto adjacente: '))
h = hypot(o, a)
print('A hipotenusa é {:.2f}'.format(h))
print('=' * 40)