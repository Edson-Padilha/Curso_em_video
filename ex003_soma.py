num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
s = num1 + num2
#print('s')
#print('A soma entre {} e {} vale {}'.format( num1 , num2 , s))
print(f'A soma entre {num1} e {num2} vale {s}') # novo modelo, coloca f antes das aspas e nome da variavel dentro das chaves
print(type(s)) # para saber qual tipo é, inteiro, real boolean ou str