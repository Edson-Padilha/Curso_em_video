from math import cos, sin, tan, radians
print('=' * 70)
num = float(input('Digite o angulo: '))
s = sin(radians(num))
c = cos(radians(num))
t = tan(radians(num))
print('O valor de seno é {:.2f} de cosseno é {:.2f} e o valor da tangente {:.2f}'.format(s, c, t))
print('=' * 70)