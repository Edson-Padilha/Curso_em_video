num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print(' Unidade: {:2}\n Dezena: {:2}\n Centena: {:2}\n Milhar:{:2}'.format (u, d, c, m))