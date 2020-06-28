cont = n = c  = soma = media = maior = menor = 0


resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    media = soma / cont

    if cont == 1:
        maior = menor = n

    else:
        if n > maior:
            maior = n

            if n < menor:
                menor = n


    resp = str(input(('Quer continuar? [S/N]: '))).upper().strip()[0]

print('Você digitou {} números e a média foi {:.2f}. \nE o maior número foi {} e o menor número foi {}.'.format(cont, media, maior, menor))


