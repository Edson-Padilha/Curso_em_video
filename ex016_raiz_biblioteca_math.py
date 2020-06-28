import math
print('=' * 40)
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('=' * 40)

#Abaixo exemplo com importaçõ somente da função especifica com arrendondamento para baixo
#from math import sqrt, floor
# num = int(input('Digite numero: ')
#raiz = sqrt(num)
#print('A raiz de {} é igual a {;.2f}'.format(num,foor(raiz)))