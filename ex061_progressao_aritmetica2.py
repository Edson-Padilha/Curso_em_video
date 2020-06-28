cont =  1

print('\033[36mGerador de PA\033[m')
print('-='*20)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
s = n1

while cont <= 10:
    print('{}'.format(s), end= ' -> ')
    cont += 1
    s += r
print('Fim')




