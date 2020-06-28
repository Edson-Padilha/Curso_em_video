print('\033[1;34m -=- \033[m'*20)
print(' '*10, '\033[4;34m Maior ou Menor \033[m')
p = int(input('\033[1;31mDigite primeiro numero: '))
s = int(input('Segundo numero: \033[m'))
if p > s:
    print('\033[4;34mO primeiro valor é maior\033[m')
elif s > p:
    print ('\033[4;34mO segundo valor é maior\033[m')
else:
    print('\033[4;34mNão existe valor maior ou menor, os dois são iguais\033[m')