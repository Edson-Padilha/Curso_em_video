print('-='*20)
print(' Gerador de PA')
print('-='*20)
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
cont = 1
s = n1
t = 11
m = 0
while cont < t:
    print('{}'.format(s), end=' >> ')
    s += razão
    cont += 1
    if cont == t:
        print('Pausa')
        m = int(input('Quantos termos quer mostrar a mais? '))
        t += m
        m += razão
        s == m

print('Operação finalizada com {} termos mostrados.'.format(cont - 1))



