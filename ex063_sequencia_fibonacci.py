
print('-='*20)
print('Sequência de Fibonacci')
print('=-'*20)
t = int(input('Quantos termos quer mostar? '))
s1 = 0
s2 = 1
s3 = 0
cont = 0

print('{} -> {}'.format(s1, s2), end='')
cont = 3
while cont <= t:
    s3 = s1 + s2
    print(' -> {}'.format(s3), end='')
    s1 = s2
    s2 = s3
    cont += 1
print('-> Fim')

