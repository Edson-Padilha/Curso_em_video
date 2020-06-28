soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('\033[1;36mA soma dos {} numeros impares multiplos de 3 é: {}\033[m'.format(cont, soma))