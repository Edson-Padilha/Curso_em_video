n = cont = soma = 0

while True:
        n = int(input('Digite um número: [999 Parar]: '))

        if n != 999:
            cont += 1
            soma += n

        if n == 999:
            break

print(f'A soma dos {cont} números, é {soma}.')
