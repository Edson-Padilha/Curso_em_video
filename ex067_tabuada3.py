
while True:
    n = int(input('Qual tabuada quer ver? '))
    print('-'*25)
    if n <= 0:
        print('Fim do programa de tabuada...')
        break
    for c in range(11):
        if n > 0:
            resultado = n * c
            print(f'{n} x {c} = {resultado}')
        if c == 10:
            print('-' * 25)


